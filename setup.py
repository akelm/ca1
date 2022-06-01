from cx_Freeze import setup, Executable

# sys.argv.append('py2exe')

data_files = [("untitled.ui")]
includefiles = ["untitled.ui"]
includes = ["matplotlib"]
# build_exe_options = {"packages": ["os"], "excludes": ["tkinter","matplotlib"]}

# buildOptions = dict(
    # packages=['tkinter', 'os', 'collections', 'xml.DOM', 'pandas', 'PIL', 'setuptools'],
    # excludes=['adodbapi', 'asyncio', 'atomicwrites', 'attr', 'babel', 'backcall', 'backports', 'bokeh', 'bottleneck',
    #           'bs4', 'certifi', 'cffi', 'chardet', 'click', 'cloudpickle', 'colorama', 'concurrent', 'cryptography',
    #           'curses', 'Cython', 'cytoolz', 'dask', 'dbm', 'defusedxml', 'distributed', 'docutils', 'et_xmlfile',
    #           'future', 'h5py', 'html', 'idna', 'importlib_metadata', 'ipykernel', 'IPython', 'ipython_genutils',
    #           'ipywidgets', 'jedi', 'jinja2', 'joblib', 'jsonschema', 'jupyter_client', 'jupyter_core', 'lib2to3',
    #           'llvmlite', 'locket', 'lxml', 'markupsafe', 'mkl_fft', 'mkl_random', 'mock', 'more_itertools', 'msgpack',
    #           'multiprocessing', 'nbconvert', 'nbformat', 'nose', 'notebook', 'numba', 'numexpr', 'numpydoc', 'olefile',
    #           'openpyxl', 'OpenSSL', 'packaging', 'parso', 'partd', 'pathlib2', 'patsy', 'pkg_resources', 'pluggy',
    #           'prometheus_client', 'prompt_toolkit', 'psutil', 'py', 'pycparser', 'pydoc_data', 'pygments', 'PyQt5',
    #           'pyreadline', 'pyrsistent', 'pywin', 'pyximport', 'qtpy', 'requests', 'scipy', 'send2trash', 'sklearn',
    #           'sortedcontainers', 'soupsieve', 'sphinx', 'sqlalchemy', 'sqlite3', 'statsmodels', 'tables', 'tblib',
    #           'terminado', 'test', 'testpath', 'toolz', 'tornado', 'traitlets', 'wcwidth', 'win32com', 'winpty',
    #           'win_unicode_console', 'wsgiref', 'xlrd', 'xlsxwriter', 'xlwt', 'xmlrpc', 'yaml', 'zict', 'zmq',
    #           '_pytest'],
    # ['adodbapi', 'asyncio', 'atomicwrites', 'attr', 'babel', 'backcall', 'backports', 'bokeh', 'bottleneck', 'bs4', 'certifi',  'cffi', 'chardet', 'click', 'cloudpickle', 'colorama', 'concurrent', 'cryptography','ctypes', 'curses', 'Cython', 'cytoolz', 'dask', 'dbm', 'defusedxml', 'distributed', 'docutils', 'et_xmlfile', 'future', 'h5py', 'html', 'importlib_metadata', 'ipywidgets', 'jedi', 'jinja2', 'joblib', 'jupyter_client', 'jupyter_core', 'lib2to3', 'llvmlite', 'locket', 'lxml', 'markupsafe', 'mkl_fft', 'mkl_random', 'mock', 'more_itertools', 'msgpack', 'multiprocessing', 'nbconvert', 'nbformat', 'nose', 'notebook', 'numba', 'numexpr', 'numpydoc', 'olefile', 'openpyxl', 'OpenSSL', 'packaging',  'parso', 'partd', 'pathlib2', 'patsy', 'pkg_resources', 'pluggy', 'prometheus_client', 'prompt_toolkit', 'psutil', 'py', 'pycparser', 'pydoc_data', 'pygments', 'PyQt5', 'pyreadline', 'pyrsistent','pywin', 'pyximport', 'qtpy', 'requests', 'scipy', 'send2trash', 'setuptools', 'sklearn', 'sortedcontainers', 'soupsieve', 'sphinx', 'sqlalchemy', 'statsmodels', 'tables', 'tblib', 'terminado', 'test', 'testpath', 'tornado', 'traitlets',  'wcwidth', 'sqlite3', 'wsgiref', 'xlrd', 'xlsxwriter', 'xlwt', 'xmlrpc', 'yaml', 'zict', 'zmq'],
# )

setup(
executables = [Executable(script = "ca_gui.py", base = "Win32GUI")],
options = {"build_exe": {'include_files':includefiles, "includes": includes}}
    )