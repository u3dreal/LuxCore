#include <string>
namespace slg { namespace ocl {
std::string KernelSource_camera_types = 
"#line 2 \"camera_types.cl\"\n"
"\n"
"/***************************************************************************\n"
" * Copyright 1998-2017 by authors (see AUTHORS.txt)                        *\n"
" *                                                                         *\n"
" *   This file is part of LuxRender.                                       *\n"
" *                                                                         *\n"
" * Licensed under the Apache License, Version 2.0 (the \"License\");         *\n"
" * you may not use this file except in compliance with the License.        *\n"
" * You may obtain a copy of the License at                                 *\n"
" *                                                                         *\n"
" *     http://www.apache.org/licenses/LICENSE-2.0                          *\n"
" *                                                                         *\n"
" * Unless required by applicable law or agreed to in writing, software     *\n"
" * distributed under the License is distributed on an \"AS IS\" BASIS,       *\n"
" * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.*\n"
" * See the License for the specific language governing permissions and     *\n"
" * limitations under the License.                                          *\n"
" ***************************************************************************/\n"
"\n"
"#define CAMERA_MAX_INTERPOLATED_TRANSFORM 8\n"
"\n"
"typedef enum {\n"
"	PERSPECTIVE, ORTHOGRAPHIC, STEREO, ENVIRONMENT\n"
"} CameraType;\n"
"\n"
"typedef struct {\n"
"	// Placed here for Transform memory alignment\n"
"	Transform rasterToCamera;\n"
"	Transform cameraToWorld;\n"
"\n"
"	float yon, hither;\n"
"	float shutterOpen, shutterClose;\n"
"\n"
"	// Used for camera motion blur\n"
"	MotionSystem motionSystem;\n"
"	InterpolatedTransform interpolatedTransforms[CAMERA_MAX_INTERPOLATED_TRANSFORM];\n"
"} CameraBase;\n"
"\n"
"typedef struct {\n"
"	// Used for camera clipping plane\n"
"	Point clippingPlaneCenter;\n"
"	Normal clippingPlaneNormal;\n"
"	// Note: preprocessor macro PARAM_CAMERA_ENABLE_CLIPPING_PLANE set if to use\n"
"	// the user defined clipping plane\n"
"\n"
"	float lensRadius;\n"
"	float focalDistance;\n"
"} ProjectiveCamera;\n"
"\n"
"typedef struct {\n"
"	ProjectiveCamera projCamera;\n"
"	\n"
"	float screenOffsetX, screenOffsetY;\n"
"	float fieldOfView;\n"
"	// Note: preprocessor macro PARAM_CAMERA_ENABLE_OCULUSRIFT_BARREL set if to use\n"
"	// Oculus Rift barrel effect\n"
"} PerspectiveCamera;\n"
"\n"
"typedef struct {\n"
"	ProjectiveCamera projCamera;\n"
"} OrthographicCamera;\n"
"\n"
"typedef struct {\n"
"	ProjectiveCamera projCamera;\n"
"} EnvironmentCamera;\n"
"\n"
"typedef struct {\n"
"	PerspectiveCamera perspCamera;\n"
"\n"
"	Transform leftEyeRasterToCamera;\n"
"	Transform leftEyeCameraToWorld;\n"
"\n"
"	Transform rightEyeRasterToCamera;\n"
"	Transform rightEyeCameraToWorld;\n"
"} StereoCamera;\n"
"\n"
"typedef struct {\n"
"	// The type of camera in use is defined by preprocessor macro:\n"
"	//  PARAM_CAMERA_TYPE (0 = Perspective, 1 = Orthographic, 2 = Stereo)\n"
"\n"
"	CameraBase base;\n"
"\n"
"	union {\n"
"		PerspectiveCamera persp;\n"
"		OrthographicCamera ortho;\n"
"		StereoCamera stereo;\n"
"		EnvironmentCamera env;\n"
"	};\n"
"} Camera;\n"
; } }
