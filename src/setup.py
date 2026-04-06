from setuptools import setup
import setup_translate

pkg = 'Extensions.ShowClock'
setup(name='enigma2-plugin-extensions-showclock',
       version='3.0',
       description="Push key 'Exit long' to show the clock while watching TV",
       package_dir={pkg: 'ShowClock'},
       packages=[pkg],
       package_data={pkg: ['images/*.png', '*.png', '*.xml', 'locale/*/LC_MESSAGES/*.mo', 'maintainer.info', 'LICENSE', 'keymap.xml', 'plugin.png']},
       cmdclass=setup_translate.cmdclass,  # for translation
      )
