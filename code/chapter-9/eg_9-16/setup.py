from setuptools import setup, Extension

setup(name='testlib',
      ext_modules=[
          Extension(name='testlib',
                    sources=['testlib_ext.c', 'testlib.c'],
                    include_dirs=['/include/path/in/python/env', '.'],
                    )
      ]
)