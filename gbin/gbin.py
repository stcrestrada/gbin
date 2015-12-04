import os

from utils import has_git_cmd, is_git_dir, git_find_files


shebang_map = {
    'js': '/usr/bin/env node',
    'py': '/usr/bin/env python'
}

GBIN_DIRS = 'gbin'
GBIN_FILE_GLOB = os.path.join('**', GBIN_DIRS, '*')
GBIN_EXCLUED_FN = {'__init__.py'}
GBIN_EXCLUDE_EXT = {'.pyc'}


class GbinException(Exception):
    pass


class GBin(object):
    def __init__(self, git_dir, glob=GBIN_FILE_GLOB, exclude_extensions=GBIN_EXCLUDE_EXT,
                 excluded_fn=GBIN_EXCLUED_FN):
        if not has_git_cmd():
            raise GbinException("No git command found.")
        if not is_git_dir(git_dir):
            raise GbinException("{} is not a git directory".format(git_dir))
        self._glob = glob
        self._ext_ex = exclude_extensions
        self._fn_ex = excluded_fn
        self.git_dir = git_dir

    def get_bins(self):
        bins = []
        potential_files = git_find_files(git_dir=self.git_dir, match=self._glob)
        for fn in potential_files:
            ext = os.path.splitext(fn)
            if ext and ext in self._ext_ex:
                continue
            if os.path.basename(fn) in GBIN_EXCLUED_FN:
                continue
            full_path = os.path.join(self.git_dir, fn)
            bins.append(Bin(full_path))
        return bins


class Bin(object):
    def __init__(self, abs_path):
        self._abs_path = abs_path
        self._inenv_name = None
        self._closes_venv =


    @property
    def abs_path(self):
        return self._abs_path


    def path_relative_to(self, start_path):
        pass

    @property
    def closest_venv(self):
        pass


    def execute(self, quiet=False):
        pass
