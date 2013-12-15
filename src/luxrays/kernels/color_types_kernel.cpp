#include <string>
namespace luxrays { namespace ocl {
std::string KernelSource_color_types = 
"#line 2 \"color_types.cl\"\n"
"\n"
"/***************************************************************************\n"
" * Copyright 1998-2013 by authors (see AUTHORS.txt)                        *\n"
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
"#if defined(SLG_OPENCL_KERNEL)\n"
"#define BLACK ((float3)(0.f, 0.f, 0.f))\n"
"#define WHITE ((float3)(1.f, 1.f, 1.f))\n"
"#endif\n"
"\n"
"#define ASSIGN_SPECTRUM(c0, c1) { (c0).c[0] = (c1).c[0]; (c0).c[1] = (c1).c[1]; (c0).c[2] = (c1).c[2]; }\n"
"\n"
"typedef struct {\n"
"	float c[3];\n"
"} RGBColor;\n"
"\n"
"typedef RGBColor Spectrum;\n"
; } }
