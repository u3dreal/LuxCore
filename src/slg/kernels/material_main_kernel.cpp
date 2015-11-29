#include <string>
namespace slg { namespace ocl {
std::string KernelSource_material_main = 
"#line 2 \"material_main.cl\"\n"
"\n"
"/***************************************************************************\n"
" * Copyright 1998-2015 by authors (see AUTHORS.txt)                        *\n"
" *                                                                         *\n"
" *   This file is part of LuxRender.                                       *\n"
" *                                                                         *\n"
" * Licensed under the Apache License, Version 2.0 (the License);         *\n"
" * you may not use this file except in compliance with the License.        *\n"
" * You may obtain a copy of the License at                                 *\n"
" *                                                                         *\n"
" *     http://www.apache.org/licenses/LICENSE-2.0                          *\n"
" *                                                                         *\n"
" * Unless required by applicable law or agreed to in writing, software     *\n"
" * distributed under the License is distributed on an AS IS BASIS,       *\n"
" * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.*\n"
" * See the License for the specific language governing permissions and     *\n"
" * limitations under the License.                                          *\n"
" ***************************************************************************/\n"
"\n"
"//------------------------------------------------------------------------------\n"
"// Main material functions\n"
"//\n"
"// This is a glue between dynamic generated code and static.\n"
"//------------------------------------------------------------------------------\n"
"\n"
"//------------------------------------------------------------------------------\n"
"// Material_IsDynamic\n"
"//------------------------------------------------------------------------------\n"
"\n"
"bool Material_IsDynamic(__global const Material *material) {\n"
"#if defined (PARAM_ENABLE_MAT_MIX) || defined (PARAM_ENABLE_MAT_GLOSSYCOATING)\n"
"		return (material->type == MIX) || (material->type == GLOSSYCOATING);\n"
"#else\n"
"		return false;\n"
"#endif\n"
"}\n"
"\n"
"//------------------------------------------------------------------------------\n"
"// Material_GetEventTypes\n"
"//------------------------------------------------------------------------------\n"
"\n"
"BSDFEvent Material_GetEventTypes(const uint matIndex\n"
"		MATERIALS_PARAM_DECL) {\n"
"	__global const Material *material = &mats[matIndex];\n"
"\n"
"	BSDFEvent result;\n"
"	if (Material_IsDynamic(material))\n"
"		result = Material_GetEventTypesWithDynamic(matIndex\n"
"			MATERIALS_PARAM);\n"
"	else\n"
"		result = Material_GetEventTypesWithoutDynamic(material);\n"
"\n"
"	return result;\n"
"}\n"
"\n"
"//------------------------------------------------------------------------------\n"
"// Material_IsDelta\n"
"//------------------------------------------------------------------------------\n"
"\n"
"bool Material_IsDelta(const uint matIndex\n"
"		MATERIALS_PARAM_DECL) {\n"
"	__global const Material *material = &mats[matIndex];\n"
"\n"
"	bool result;\n"
"	if (Material_IsDynamic(material))\n"
"		result = Material_IsDeltaWithDynamic(matIndex\n"
"			MATERIALS_PARAM);\n"
"	else\n"
"		result = Material_IsDeltaWithoutDynamic(material);\n"
"\n"
"	return result;\n"
"}\n"
"\n"
"//------------------------------------------------------------------------------\n"
"// Material_Evaluate\n"
"//------------------------------------------------------------------------------\n"
"\n"
"float3 Material_Evaluate(const uint matIndex,\n"
"		__global HitPoint *hitPoint, const float3 lightDir, const float3 eyeDir,\n"
"		BSDFEvent *event, float *directPdfW\n"
"		MATERIALS_PARAM_DECL) {\n"
"	return Material_EvaluateWithDynamic(matIndex, hitPoint,\n"
"			lightDir, eyeDir,\n"
"			event, directPdfW\n"
"			MATERIALS_PARAM);\n"
"}\n"
"\n"
"//------------------------------------------------------------------------------\n"
"// Material_Sample\n"
"//------------------------------------------------------------------------------\n"
"\n"
"//float3 Material_Sample(const uint matIndex, __global HitPoint *hitPoint,\n"
"//		const float3 fixedDir, float3 *sampledDir,\n"
"//		const float u0, const float u1,\n"
"//#if defined(PARAM_HAS_PASSTHROUGH)\n"
"//		const float passThroughEvent,\n"
"//#endif\n"
"//		float *pdfW, float *cosSampledDir, BSDFEvent *event,\n"
"//		const BSDFEvent requestedEvent\n"
"//		MATERIALS_PARAM_DECL) {\n"
"//	__global const Material *material = &mats[matIndex];\n"
"//\n"
"//	if (Material_IsDynamic(material))\n"
"//		return Material_SampleWithDynamic(mat, hitPoint, fixedDir, sampledDir, u0, u1,\n"
"//#if defined(PARAM_HAS_PASSTHROUGH)\n"
"//				passThroughEvent,\n"
"//#endif\n"
"//				pdfW,  cosSampledDir, event, requestedEvent\n"
"//				MATERIALS_PARAM);\n"
"//	else\n"
"//		return Material_SampleWithoutDynamic(mat, hitPoint, fixedDir, sampledDir, u0, u1,\n"
"//#if defined(PARAM_HAS_PASSTHROUGH)\n"
"//				passThroughEvent,\n"
"//#endif\n"
"//				pdfW,  cosSampledDir, event, requestedEvent\n"
"//				MATERIALS_PARAM);\n"
"//}\n"
"\n"
"float3 Material_Sample(const uint matIndex, __global HitPoint *hitPoint,\n"
"		const float3 fixedDir, float3 *sampledDir,\n"
"		const float u0, const float u1,\n"
"#if defined(PARAM_HAS_PASSTHROUGH)\n"
"		const float passThroughEvent,\n"
"#endif\n"
"		float *pdfW, float *cosSampledDir, BSDFEvent *event,\n"
"		const BSDFEvent requestedEvent\n"
"		MATERIALS_PARAM_DECL) {\n"
"	return Material_SampleWithDynamic(matIndex, hitPoint, fixedDir, sampledDir, u0, u1,\n"
"#if defined(PARAM_HAS_PASSTHROUGH)\n"
"			passThroughEvent,\n"
"#endif\n"
"			pdfW,  cosSampledDir, event, requestedEvent\n"
"			MATERIALS_PARAM);\n"
"}\n"
"\n"
"//------------------------------------------------------------------------------\n"
"// Material_GetPassThroughTransparency\n"
"//------------------------------------------------------------------------------\n"
"\n"
"#if defined(PARAM_HAS_PASSTHROUGH)\n"
"float3 Material_GetPassThroughTransparency(const uint matIndex, __global HitPoint *hitPoint,\n"
"		const float3 localFixedDir, const float passThroughEvent\n"
"		MATERIALS_PARAM_DECL) {\n"
"	__global const Material *material = &mats[matIndex];\n"
"\n"
"	float3 result;\n"
"	if (Material_IsDynamic(material))\n"
"		result = Material_GetPassThroughTransparencyWithDynamic(matIndex, hitPoint,\n"
"			localFixedDir, passThroughEvent\n"
"			MATERIALS_PARAM);\n"
"	else\n"
"		result = Material_GetPassThroughTransparencyWithoutDynamic(material, hitPoint,\n"
"			localFixedDir, passThroughEvent\n"
"			MATERIALS_PARAM);\n"
"\n"
"	return result;\n"
"}\n"
"#endif\n"
"\n"
"//------------------------------------------------------------------------------\n"
"// Material_GetEmittedRadiance\n"
"//------------------------------------------------------------------------------\n"
"\n"
"float3 Material_GetEmittedRadiance(const uint matIndex,\n"
"		__global HitPoint *hitPoint, const float oneOverPrimitiveArea\n"
"		MATERIALS_PARAM_DECL) {\n"
"	__global const Material *material = &mats[matIndex];\n"
"\n"
"	float3 result;\n"
"	if (Material_IsDynamic(material))\n"
"		result = Material_GetEmittedRadianceWithDynamic(matIndex, hitPoint\n"
"			MATERIALS_PARAM);\n"
"	else\n"
"		result = Material_GetEmittedRadianceWithoutDynamic(material, hitPoint\n"
"			TEXTURES_PARAM);\n"
"\n"
"	return VLOAD3F(material->emittedFactor.c) * (material->usePrimitiveArea ? oneOverPrimitiveArea : 1.f) * result;\n"
"}\n"
"\n"
"//------------------------------------------------------------------------------\n"
"// Material_GetInteriorVolume\n"
"//------------------------------------------------------------------------------\n"
"\n"
"#if defined(PARAM_HAS_VOLUMES)\n"
"uint Material_GetInteriorVolume(const uint matIndex,\n"
"		__global HitPoint *hitPoint\n"
"#if defined(PARAM_HAS_PASSTHROUGH)\n"
"		, const float passThroughEvent\n"
"#endif\n"
"		MATERIALS_PARAM_DECL) {\n"
"	__global const Material *material = &mats[matIndex];\n"
"\n"
"	if (Material_IsDynamic(material))\n"
"		return Material_GetInteriorVolumeWithDynamic(matIndex, hitPoint\n"
"#if defined(PARAM_HAS_PASSTHROUGH)\n"
"			, passThroughEvent\n"
"#endif\n"
"			MATERIALS_PARAM);\n"
"	else\n"
"		return Material_GetInteriorVolumeWithoutDynamic(material);\n"
"}\n"
"#endif\n"
"\n"
"//------------------------------------------------------------------------------\n"
"// Material_GetExteriorVolume\n"
"//------------------------------------------------------------------------------\n"
"\n"
"#if defined(PARAM_HAS_VOLUMES)\n"
"uint Material_GetExteriorVolume(const uint matIndex,\n"
"		__global HitPoint *hitPoint\n"
"#if defined(PARAM_HAS_PASSTHROUGH)\n"
"		, const float passThroughEvent\n"
"#endif\n"
"		MATERIALS_PARAM_DECL) {\n"
"	__global const Material *material = &mats[matIndex];\n"
"	\n"
"	if (Material_IsDynamic(material))\n"
"		return Material_GetExteriorVolumeWithDynamic(matIndex, hitPoint\n"
"#if defined(PARAM_HAS_PASSTHROUGH)\n"
"			, passThroughEvent\n"
"#endif\n"
"			MATERIALS_PARAM);\n"
"	else\n"
"		return Material_GetExteriorVolumeWithoutDynamic(material);\n"
"}\n"
"#endif\n"
"\n"
"//------------------------------------------------------------------------------\n"
"// Material_Bump\n"
"//------------------------------------------------------------------------------\n"
"\n"
"#if defined(PARAM_HAS_BUMPMAPS)\n"
"void Material_Bump(const uint matIndex, __global HitPoint *hitPoint\n"
"	MATERIALS_PARAM_DECL) {\n"
"	const uint bumpTexIndex = mats[matIndex].bumpTexIndex;\n"
"	\n"
"	if (bumpTexIndex != NULL_INDEX) {\n"
"		float3 shadeN = VLOAD3F(&hitPoint->shadeN.x);\n"
"\n"
"		shadeN = Texture_Bump(mats[matIndex].bumpTexIndex, hitPoint, mats[matIndex].bumpSampleDistance\n"
"			TEXTURES_PARAM);\n"
"\n"
"		// Update dpdu and dpdv so they are still orthogonal to shadeN\n"
"		float3 dpdu = VLOAD3F(&hitPoint->dpdu.x);\n"
"		float3 dpdv = VLOAD3F(&hitPoint->dpdv.x);\n"
"		dpdu = cross(shadeN, cross(dpdu, shadeN));\n"
"		dpdv = cross(shadeN, cross(dpdv, shadeN));\n"
"		// Update HitPoint structure\n"
"		VSTORE3F(shadeN, &hitPoint->shadeN.x);\n"
"		VSTORE3F(dpdu, &hitPoint->dpdu.x);\n"
"		VSTORE3F(dpdv, &hitPoint->dpdv.x);\n"
"	}\n"
"}\n"
"#endif\n"
; } }
