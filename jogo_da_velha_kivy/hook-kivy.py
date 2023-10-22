from kivy.tools.packaging.pyinstaller_hooks import (
    add_dep_paths, excludedimports, datas, get_deps_all,
    get_factory_modules, kivy_modules)

add_dep_paths()

hiddenimports = get_deps_all()['hiddenimports']
hiddenimports = list(set(
    get_factory_modules() + kivy_modules + hiddenimports))


hiddenimports += [
    'kivy.core',

    'kivy.core.audio',

    'kivy.core.audio.audio_android',
    'kivy.core.audio.audio_avplayer',
    'kivy.core.audio.audio_ffpyplayer',
    'kivy.core.audio.audio_gstplayer',
    'kivy.core.audio.audio_pygame',
    'kivy.core.audio.audio_sdl2',

    'kivy.core.camera',

    'kivy.core.camera.camera_android',
    'kivy.core.camera.camera_gi',
    'kivy.core.camera.camera_opencv',
    'kivy.core.camera.camera_picamera',

    'kivy.core.clipboard',

    'kivy.core.clipboard._clipboard_ext',
    'kivy.core.clipboard._clipboard_sdl2',
    'kivy.core.clipboard.clipboard_android',
    'kivy.core.clipboard.clipboard_dbusklipper',
    'kivy.core.clipboard.clipboard_dummy',
    'kivy.core.clipboard.clipboard_gtk3',
    'kivy.core.clipboard.clipboard_nspaste',
    'kivy.core.clipboard.clipboard_pygame',
    'kivy.core.clipboard.clipboard_sdl2',
    'kivy.core.clipboard.clipboard_winctypes',
    'kivy.core.clipboard.clipboard_xclip',
    'kivy.core.clipboard.clipboard_xsel',

    'kivy.core.gl',
    'kivy.core.image',

    'kivy.core.image._img_sdl2',
    'kivy.core.image.img_dds',
    'kivy.core.image.img_ffpyplayer',
    'kivy.core.image.img_pil',
    'kivy.core.image.img_pygame',
    'kivy.core.image.img_sdl2',
    'kivy.core.image.img_tex',

    'kivy.core.spelling',

    'kivy.core.spelling.spelling_enchant',
    'kivy.core.spelling.spelling_osxappkit',

    'kivy.core.text',

    'kivy.core.text._text_sdl2',
    'kivy.core.text.markup',
    'kivy.core.text.text_layout',
    'kivy.core.text.text_pango',
    'kivy.core.text.text_pil',
    'kivy.core.text.text_pygame',
    'kivy.core.text.text_sdl2',

    'kivy.core.video',

    'kivy.core.video.video_ffmpeg',
    'kivy.core.video.video_ffpyplayer',
    'kivy.core.video.video_gstplayer',
    'kivy.core.video.video_null',

    'kivy.core.window',

    'kivy.core.window._window_sdl2',
    'kivy.core.window.window_egl_rpi',
    'kivy.core.window.window_info',
    'kivy.core.window.window_pygame',
    'kivy.core.window.window_sdl2',

    'kivy.graphics',

    'kivy.graphics.boxshadow',
    'kivy.graphics.buffer',
    'kivy.graphics.cgl',
    'kivy.graphics.cgl_backend',

    'kivy.graphics.cgl_backend.cgl_debug',
    'kivy.graphics.cgl_backend.cgl_gl',
    'kivy.graphics.cgl_backend.cgl_glew',
    'kivy.graphics.cgl_backend.cgl_mock',
    'kivy.graphics.cgl_backend.cgl_sdl2',

    'kivy.graphics.compiler',
    'kivy.graphics.context',
    'kivy.graphics.context_instructions',
    'kivy.graphics.fbo',
    'kivy.graphics.gl_instructions',
    'kivy.graphics.instructions',
    'kivy.graphics.opengl',
    'kivy.graphics.opengl_utils',
    'kivy.graphics.scissor_instructions',
    'kivy.graphics.shader',
    'kivy.graphics.stencil_instructions',
    'kivy.graphics.svg',
    'kivy.graphics.tesselator',
    'kivy.graphics.texture',
    'kivy.graphics.transformation',
    'kivy.graphics.vbo',
    'kivy.graphics.vertex',
    'kivy.graphics.vertex_instructions',

    'kivy.weakmethod',

    'xml.etree.cElementTree'
]
