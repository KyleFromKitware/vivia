project(vsKstArchiveSource)

include_directories(
  ${CMAKE_CURRENT_SOURCE_DIR}
  ${CMAKE_CURRENT_BINARY_DIR}
)
vg_include_library_sdk_directories(vspSourceUtil)

set(vsKstArchiveSource_Sources
  vsKstArchiveSourcePlugin.cxx
  vsKstDescriptorArchiveSource.cxx
)

set(vsKstArchiveSource_MocHeaders
  vsKstArchiveSourcePlugin.h
  vsKstDescriptorArchiveSource.h
)

qt4_wrap_cpp(vsKstArchiveSource_MocSources ${vsKstArchiveSource_MocHeaders})

vg_add_qt_plugin(${PROJECT_NAME}
  ${vsKstArchiveSource_Sources}
  ${vsKstArchiveSource_MocSources}
)

target_link_libraries(${PROJECT_NAME}
  vspSourceUtil
  vvIO
  ${QT_LIBRARIES}
)

install_plugin_targets(${PROJECT_NAME})
