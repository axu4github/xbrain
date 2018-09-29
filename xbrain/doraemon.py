# coding=utf-8

import os


class Doraemon(object):
    """Python 工具集"""

    @staticmethod
    def get_files_by_suffix(_dir, suffix=None):
        file_filter = None
        if suffix is not None:
            def suffix_filter_fn(fpath):
                return suffix.lower() == os.path.splitext(fpath)[-1].lower()

            file_filter = suffix_filter_fn

        return Doraemon.get_files(_dir, file_filter=file_filter)

    @staticmethod
    def get_files(_dir, file_filter=None):
        match_files = []
        if os.path.isfile(_dir):
            match_files.append(_dir)
        else:
            for root, dirs, files in os.walk(_dir):
                if file_filter is not None:
                    files = filter(file_filter, files)

                for fname in files:
                    match_files.append(os.path.join(root, fname))

        return match_files

    @staticmethod
    def get_file_contents(fpath, in_charset=None, out_charset=None):
        contents = []
        with open(fpath, "r") as f:
            for content in f.readlines():
                if in_charset is not None and out_charset is not None:
                    content = content.decode(in_charset).encode(out_charset)

                contents.append(content.strip())

        return contents

    @staticmethod
    def put_file_contents(fpath, contents):
        with open(fpath, "w") as f:
            if isinstance(contents, list):
                for content in contents:
                    f.write("{0}{1}".format(content, os.linesep))
            else:
                f.write(contents)

        return True
