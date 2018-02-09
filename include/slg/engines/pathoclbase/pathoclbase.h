/***************************************************************************
 * Copyright 1998-2018 by authors (see AUTHORS.txt)                        *
 *                                                                         *
 *   This file is part of LuxCoreRender.                                   *
 *                                                                         *
 * Licensed under the Apache License, Version 2.0 (the "License");         *
 * you may not use this file except in compliance with the License.        *
 * You may obtain a copy of the License at                                 *
 *                                                                         *
 *     http://www.apache.org/licenses/LICENSE-2.0                          *
 *                                                                         *
 * Unless required by applicable law or agreed to in writing, software     *
 * distributed under the License is distributed on an "AS IS" BASIS,       *
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.*
 * See the License for the specific language governing permissions and     *
 * limitations under the License.                                          *
 ***************************************************************************/

#ifndef _SLG_PATHOCLBASE_H
#define	_SLG_PATHOCLBASE_H

#if !defined(LUXRAYS_DISABLE_OPENCL)

#include "luxrays/core/intersectiondevice.h"
#include "luxrays/utils/ocl.h"

#include "slg/slg.h"
#include "slg/engines/oclrenderengine.h"
#include "slg/engines/pathoclbase/pathoclbasethread.h"
#include "slg/engines/pathtracer.h"

namespace slg {

//------------------------------------------------------------------------------
// Path Tracing 100% OpenCL render engine
// (base class for all types of OCL path tracers)
//------------------------------------------------------------------------------

class PathOCLBaseRenderEngine : public OCLRenderEngine {
public:
	PathOCLBaseRenderEngine(const RenderConfig *cfg, Film *flm, boost::mutex *flmMutex);
	virtual ~PathOCLBaseRenderEngine();

	virtual bool IsMaterialCompiled(const MaterialType type) const {
		return (compiledScene == NULL) ? false : compiledScene->IsMaterialCompiled(type);
	}

	virtual bool HasDone() const;
	virtual void WaitForDone() const;

	friend class PathOCLBaseRenderThread;

	size_t maxMemPageSize;
	u_int taskCount;
	bool usePixelAtomics;

	PathTracer pathTracer;

protected:
	virtual PathOCLBaseRenderThread *CreateOCLThread(const u_int index, luxrays::OpenCLIntersectionDevice *device) = 0;

	void InitPixelFilterDistribution();

	void InitFilm();
	void StartLockLess();
	void StopLockLess();

	void BeginSceneEditLockLess();
	void EndSceneEditLockLess(const EditActionList &editActions);

	boost::mutex setKernelArgsMutex;

	CompiledScene *compiledScene;

	std::vector<PathOCLBaseRenderThread *> renderThreads;
	
	std::string additionalKernelOptions;
	bool writeKernelsToFile;

	// Pixel filter related variables
	float *pixelFilterDistribution;
	u_int pixelFilterDistributionSize;

	slg::ocl::Sampler *oclSampler;
	slg::ocl::Filter *oclPixelFilter;
};

}

#endif

#endif	/* _SLG_PATHOCLBASE_H */
