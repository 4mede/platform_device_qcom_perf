#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2025-2026 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.fixups_lib import (
    lib_fixup_remove,
    lib_fixups,
    lib_fixups_user_type,
)

from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    'hardware/qcom-caf/wlan',
    'vendor/qcom/opensource/commonsys/display',
    'vendor/qcom/opensource/commonsys-intf/display',
    'vendor/qcom/opensource/display',
    'vendor/qcom/opensource/dataservices',
    'vendor/qcom/perf',
]


libs_add_vendor_suffix = (
    'vendor.qti.hardware.iop@2.0',
    'vendor.qti.hardware.perf@2.0',
    'vendor.qti.hardware.perf@2.1',
    'vendor.qti.hardware.perf@2.2',
    'vendor.qti.hardware.perf2-V1-ndk',
    'vendor.qti.qspmhal-V1-ndk',
)

libs_remove = (
'libthermalclient'
)

def lib_fixup_vendor_suffix(lib: str, partition: str, *args, **kwargs):
    if partition != 'vendor':
        return None

    return f'{lib}_{partition}'


lib_fixups: lib_fixups_user_type = {
    **lib_fixups,
    libs_add_vendor_suffix: lib_fixup_vendor_suffix,
    libs_remove: lib_fixup_remove,
}


blob_fixups: blob_fixups_user_type = {
     'vendor/lib64/libaodoptfeature.so': blob_fixup()
        .replace_needed('vendor.qti.hardware.display.config-V5-ndk.so', 'vendor.qti.hardware.display.config-V12-ndk.so'),
    'vendor/lib64/libapengine.so': blob_fixup()
        .replace_needed('vendor.qti.hardware.display.config-V5-ndk.so', 'vendor.qti.hardware.display.config-V12-ndk.so'),
    'vendor/lib64/libgamepoweroptfeature.so': blob_fixup()
        .replace_needed('vendor.qti.hardware.display.config-V5-ndk.so', 'vendor.qti.hardware.display.config-V12-ndk.so'),
    'vendor/lib64/liboffscreenpoweroptfeature.so': blob_fixup()
        .replace_needed('vendor.qti.hardware.display.config-V5-ndk.so', 'vendor.qti.hardware.display.config-V12-ndk.so'),
    'vendor/lib64/libpsmoptfeature.so': blob_fixup()
        .replace_needed('vendor.qti.hardware.display.config-V5-ndk.so', 'vendor.qti.hardware.display.config-V12-ndk.so'),
    'vendor/lib64/libqti-perfd.so': blob_fixup()
        .replace_needed('vendor.qti.hardware.display.config-V5-ndk.so', 'vendor.qti.hardware.display.config-V12-ndk.so'),
    'vendor/lib64/libvideooptfeature.so': blob_fixup()
        .replace_needed('vendor.qti.hardware.display.config-V5-ndk.so', 'vendor.qti.hardware.display.config-V12-ndk.so'),
} # fmt: skip

module = ExtractUtilsModule(
    'perf',
    'qcom',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()
