#! /usr/bin/python2
#-*- coding: utf-8 -*-

from PySide import QtGui, QtCore

import os
import shutil
import logging

from ..methods.decorators import Decorator
from ..methods.dialogs import Dialogs


# Python3 compatibility
if os.getenv("PINGUINO_PYTHON") is "3":
    #Python3
    from configparser import RawConfigParser
else:
    #Python2
    from ConfigParser import RawConfigParser


########################################################################
class ProjectManager(object):
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """"""
        self.connect(self.main.actionAdd_existing_directory, QtCore.SIGNAL("triggered()"), self.select_existing_directory)
        self.connect(self.main.actionNew_project, QtCore.SIGNAL("triggered()"), self.new_project)
        self.connect(self.main.actionNew_library, QtCore.SIGNAL("triggered()"), self.new_library)
        self.connect(self.main.pushButton_newproject, QtCore.SIGNAL("clicked()"), self.new_project)
        self.connect(self.main.pushButton_openproject, QtCore.SIGNAL("clicked()"), self.open_project)
        self.connect(self.main.pushButton_newlibrary, QtCore.SIGNAL("clicked()"), self.new_library)
        self.connect(self.main.actionClose_project, QtCore.SIGNAL("triggered()"), self.close_project)
        self.connect(self.main.actionSave_project, QtCore.SIGNAL("triggered()"), self.save_project)
        self.connect(self.main.actionSave_project_as, QtCore.SIGNAL("triggered()"), self.save_project_as)
        self.connect(self.main.actionAdd_current_file, QtCore.SIGNAL("triggered()"), self.add_current_file)
        self.connect(self.main.actionOpen_project, QtCore.SIGNAL("triggered()"), self.open_project)
        self.connect(self.main.actionAdd_existing_file, QtCore.SIGNAL("triggered()"), self.select_existing_file)
        self.connect(self.main.treeWidget_projects, QtCore.SIGNAL("itemExpanded(QTreeWidgetItem*)"), self.expand_tree)
        self.connect(self.main.treeWidget_projects, QtCore.SIGNAL("itemDoubleClicked(QTreeWidgetItem*,int)"), self.open_from_tree)



        self.connect(self.main.pushButton_compilelibrary, QtCore.SIGNAL("clicked()"), self.compile_library)

        self.connect(self.main.treeWidget_projects, QtCore.SIGNAL("itemChanged(QTreeWidgetItem*,int)"), self.update_check_status)


    #----------------------------------------------------------------------
    @Decorator.show_tab("Project")
    def open_project(self):

        self.project_saved = True

        file_project = Dialogs.set_open_file(self, exts="*.ppde")
        if file_project is None: return
        self.open_project_from_path(file_project)


    #----------------------------------------------------------------------
    @Decorator.show_tab("Project")
    def open_project_from_path(self, filename):
        """"""
        self.project_saved = True
        self.ConfigProject = RawConfigParser()
        self.ConfigProject.readfp(open(filename, "r"))
        self.ConfigProject.filename = filename

        project_name = self.reload_project()
        logging.debug("Opening \"{}\" project.".format(project_name))

        self.update_recents_projects(self.ConfigProject.filename)


    #----------------------------------------------------------------------
    def reload_project(self):
        """"""
        self.main.treeWidget_projects.clear()

        project_name = self.ConfigProject.get("Main", "name")
        self.main.treeWidget_projects.setHeaderLabel(project_name)

        if not self.ConfigProject.has_section("Ignore"): to_ignore = []
        elif not self.ConfigProject.options("Ignore"): to_ignore = []
        else: to_ignore = [self.ConfigProject.get("Ignore", option) for option in self.ConfigProject.options("Ignore")]

        inherits_status = self.get_inherits_from_project()

        for option in self.ConfigProject.options("Dirs"):
            if not self.ConfigProject.get("Dirs", option) in to_ignore:
                self.add_existing_directory(self.ConfigProject.get("Dirs", option), to_ignore, check_duplicated=False, inherits_status=inherits_status, open_=True)

        for path, checked in self.get_files_from_project().items():
            if path in to_ignore: continue
            self.add_existing_file(path, check_duplicated=False, check=checked, open_=True)

        self.update_project_status(project_name)
        return project_name


    #----------------------------------------------------------------------
    def select_existing_directory(self):
        """"""
        dir_project = Dialogs.set_open_dir(self)
        if dir_project in self.get_dirs_from_project(): return False

        self.add_existing_directory(dir_project, inherits_status=True)
        return dir_project



    #----------------------------------------------------------------------
    def add_existing_directory(self, dir_project, to_ignore=[], check_duplicated=True, inherits_status=dict(), open_=False):
        """"""
        self.take_from_ignore(dir_project)
        if check_duplicated:
            if dir_project in self.get_dirs_from_project(): return

        # flags = QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled
        flags = QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled
        parent = self.add_new_tree(os.path.basename(dir_project), self.main.treeWidget_projects, dir_project, flags)
        inherits = self.generate_tree(dir_project, parent, levels=50, flags=flags, to_ignore=to_ignore, inherits_status=inherits_status)
        parent.setExpanded(True)

        if not open_:
            self.add_dir_to_config(dir_project)
            self.add_inherits_to_config(inherits)


    #----------------------------------------------------------------------
    def add_current_file(self):
        """"""
        editor = self.get_tab().currentWidget()
        self.add_existing_file(editor.path)


    #----------------------------------------------------------------------
    def select_existing_file(self):
        """"""
        new_file = Dialogs.set_open_file(self)
        if new_file in self.get_files_from_project(): return
        self.add_existing_file(new_file)


    #----------------------------------------------------------------------
    def add_existing_file(self, path, check_duplicated=True, check=True, open_=False):
        """"""
        self.take_from_ignore(path)
        if check_duplicated:
            if path in self.get_files_from_project(): return

        filename = os.path.split(path)[1]
        parent = self.main.treeWidget_projects
        # flags = QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled
        flags = QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled

        self.add_new_file_item(filename, parent, path, flags, check=check)

        if not open_:
            self.add_file_to_config(path)



    #----------------------------------------------------------------------
    def set_project_name(self, library=False):
        """"""
        if library: type_ = "Library"
        else: type_ = "Project"


        project_name = Dialogs.get_text(self, "{} name".format(type_), default="untitled_{}".format(type_.lower()))

        if project_name is False:
            return

        self.main.treeWidget_projects.setHeaderLabel(project_name)

        if not self.ConfigProject.has_section("Main"): self.ConfigProject.add_section("Main")
        options = self.ConfigProject.options("Main")
        self.ConfigProject.set("Main", "name", project_name)
        self.ConfigProject.set("Main", "library", library)

        self.main.widget_library.setVisible(library)

        self.save_project(default=True)

        logging.debug("Created \"{}\" {}.".format(project_name, type_.lower()))

        return project_name
        # self.main.treeWidget_projects.setHeaderLabel(project_name)


    #----------------------------------------------------------------------
    def is_library(self):
        """"""
        if os.environ.get("PINGUINO_PROJECT", False):
            return self.ConfigProject.get("Main", "library")
        else:
            return False



    #----------------------------------------------------------------------
    def get_project_name(self):
        """"""
        return self.main.treeWidget_projects.headerItem().text(0)


    #----------------------------------------------------------------------
    def get_project_files(self):
        """"""
        files = [file_ for file_, checked in self.get_files_from_project().iteritems() if checked]
        files.extend([file_ for file_, checked in self.get_inherits_from_project().iteritems() if checked])
        return files


    # #----------------------------------------------------------------------
    # def get_main_upload(self):
        # """"""
        # header = self.main.treeWidget_projects.header()
        # filename = self.get_tab().currentWidget().path
        # return getattr(header, "main_upload", filename)


    #----------------------------------------------------------------------
    @Decorator.show_tab("Project")
    def new_project(self):
        """"""
        self.project_saved = False
        self.ConfigProject = RawConfigParser()
        project_name = self.set_project_name()

        if project_name:
            add_dir = Dialogs.confirm_message(self, QtGui.QApplication.translate("Dialogs", "Do you want add an existing directory now?"))
            if add_dir: self.select_existing_directory()
            self.update_project_status(project_name)


    #----------------------------------------------------------------------
    def save_project_as(self):
        """"""
        self.project_saved = False
        self.save_project(silent=False)



    #----------------------------------------------------------------------
    def save_project(self, silent=False, default=False):
        """"""

        if default:
            default_path = os.path.join(os.getenv("PINGUINO_USER_PATH"), "projects")

            if not os.path.exists(default_path):
                os.mkdir(default_path)
            self.ConfigProject.filename = os.path.join(default_path, self.get_project_name())
            self.ConfigProject.write(open(self.ConfigProject.filename, "w"))
            self.project_saved = True
            return

        if self.project_saved:
            self.ConfigProject.write(open(self.ConfigProject.filename, "w"))

        elif not silent:
            save = Dialogs.set_save_file(self, self.get_project_name()+".ppde")
            if save[0]:
                path, filename = save
                self.ConfigProject.filename = path
                self.ConfigProject.write(open(self.ConfigProject.filename, "w"))
                self.project_saved = True

        self.update_recents_projects(self.ConfigProject.filename)


    #----------------------------------------------------------------------
    def add_dir_to_config(self, dirpath):
        """"""
        if not self.ConfigProject.has_section("Dirs"): self.ConfigProject.add_section("Dirs")
        options = self.ConfigProject.options("Dirs")

        if dirpath in self.get_dirs_from_project(): return

        index = 0
        while "dir_%d"%index in options:
            index += 1

        self.ConfigProject.set("Dirs", "dir_%d"%index, dirpath)
        self.save_project(silent=True)


    #----------------------------------------------------------------------
    def add_inherits_to_config(self, inherits):
        """"""
        if not self.ConfigProject.has_section("Inherits"): self.ConfigProject.add_section("Inherits")
        options = self.ConfigProject.options("Inherits")

        index = 0
        while "inherit__%d"%index in options:
            index += 1

        for path in inherits:
            if path in self.get_inherits_from_project(): continue
            self.ConfigProject.set("Inherits", "inherit_%d"%index, path)
            self.ConfigProject.set("Inherits", "inherit_%d_checked"%index, "1")
            index += 1
        self.save_project(silent=True)


    #----------------------------------------------------------------------
    def add_file_to_config(self, filepath):
        """"""
        if not self.ConfigProject.has_section("Files"): self.ConfigProject.add_section("Files")
        options = self.ConfigProject.options("Files")

        if filepath in self.get_files_from_project(): return

        index = 0
        while "file_%d"%index in options:
            index += 1

        self.ConfigProject.set("Files", "file_%d"%index, filepath)
        self.ConfigProject.set("Files", "file_%d_checked"%index, "1")

        self.save_project(silent=True)


    #----------------------------------------------------------------------
    def hide_element_to_config(self, path):
        """"""
        if not self.ConfigProject.has_section("Ignore"): self.ConfigProject.add_section("Ignore")
        options = self.ConfigProject.options("Ignore")

        index = 0
        while "ignore_%d"%index in options:
            index += 1

        self.ConfigProject.set("Ignore", "ignore_%d"%index, path)

        logging.debug("Removing \"{}\" from project.".format(path))
        for path_inherit, option in self.get_inherits_option_from_project().items():
            if path_inherit.startswith(path):
                self.ConfigProject.remove_option("Inherits", option)
                self.ConfigProject.remove_option("Inherits", option+"_checked")
                logging.debug("Removing \"{}\" from project.".format(path_inherit))

        self.save_project(silent=True)


    #----------------------------------------------------------------------
    def update_project_status(self, project="reload"):
        """"""
        if project == "reload": pass
        elif project:os.environ["PINGUINO_PROJECT"] = project
        else: os.environ["PINGUINO_PROJECT"] = ""

        self.main.treeWidget_projects.setVisible(bool(project))
        self.main.widget_noproject.setVisible(not bool(project))
        self.main.widget_library.setVisible(self.is_library())

        self.main.treeWidget_projects.contextMenuEvent = self.project_context_menu
        Decorator.update_toolbar()

        open_project = bool(os.environ["PINGUINO_PROJECT"])
        self.main.actionNew_project.setEnabled(not open_project)
        self.main.actionOpen_project.setEnabled(not open_project)
        self.main.actionSave_project.setEnabled(open_project)
        self.main.actionSave_project_as.setEnabled(open_project)
        self.main.actionClose_project.setEnabled(open_project)
        self.main.actionAdd_existing_directory.setEnabled(open_project)
        self.main.actionAdd_current_file.setEnabled(open_project)
        self.main.actionAdd_existing_file.setEnabled(open_project)
        self.main.actionAdd_new_file.setEnabled(open_project)
        # self.main.actionSet_current_file_as_main_upload.setEnabled(open_project)



    #----------------------------------------------------------------------
    def get_current_item(self):
        """"""
        return self.main.treeWidget_projects.currentItem()




    #----------------------------------------------------------------------
    def project_context_menu(self, event):
        menu = QtGui.QMenu()

        if hasattr(self.get_current_item(), "path"):
            if os.path.isfile(self.get_current_item().path):
                # option for files
                # menu.addAction("Set as main upload file", self.set_as_main_upload)
                menu.addAction("Remove file", self.remove_file)
            else:
                # option for dirs
                menu.addAction("Remove directory", self.remove_directory)

            # option for files and dirs
            menu.addAction("Remove exclude from project", self.remove_from_tree)

        # general options
        menu.addAction("Rename...", self.rename)
        menu.addSeparator()
        menu.addAction("Add existing directory...", self.select_existing_directory)
        menu.addAction("Add existing file...", self.select_existing_file)
        menu.addSeparator()
        if hasattr(self.get_current_item(), "path"):
            menu.addAction("Add new file...", self.add_new_file)
            menu.addAction("Add new blocks file...", self.add_new_blocks_file)
            menu.addAction("Add new directory...", self.add_new_directory)
        menu.addAction("Close project", self.close_project)
        menu.addAction("Open project...", self.open_project)
        menu.addSeparator()
        menu.addAction("Reload project", self.reload_project)

        menu.setStyleSheet("""
        QMenu {
            font-family: inherit;
            font-weight: normal;
            }

        """)

        menu.exec_(event.globalPos())


    # #----------------------------------------------------------------------
    # def set_as_main_upload(self):
        # """"""
        # item = self.get_current_item()
        # item.setForeground(0, QtGui.QColor("#FF0000"))

        # item.setText(0, "{} [main upload file]".format(item.text(0)))

        # if not self.ConfigProject.has_section("Main"): self.ConfigProject.add_section("Main")
        # self.ConfigProject.set("Main", "main_upload", item.path)
        # self.save_project(True)

        # header = self.main.treeWidget_projects.header()
        # header.main_upload = item.path


    #----------------------------------------------------------------------
    def remove_file(self):
        """"""
        item = self.get_current_item()
        os.remove(item.path)
        item.removeChild(item)


    #----------------------------------------------------------------------
    def remove_directory(self):
        """"""
        item = self.get_current_item()
        shutil.rmtree(item.path)
        item.removeChild(item)


    #----------------------------------------------------------------------
    def remove_from_tree(self):
        """"""
        item = self.get_current_item()
        self.hide_element_to_config(item.path)
        item.removeChild(item)


    #----------------------------------------------------------------------
    def take_from_ignore(self, path):
        """"""
        if self.ConfigProject.has_section("Ignore"):
            options = self.ConfigProject.options("Ignore")
            for option in options:
                if self.ConfigProject.get("Ignore", option) == path:
                    self.ConfigProject.remove_option("Ignore", option)


    #----------------------------------------------------------------------
    def get_dirs_from_project(self):
        """"""
        if not self.ConfigProject.has_section("Dirs"): return []
        if not self.ConfigProject.options("Dirs"): return []
        return [self.ConfigProject.get("Dirs", option) for option in self.ConfigProject.options("Dirs")]


    #----------------------------------------------------------------------
    def get_ignore_from_project(self):
        """"""
        if not self.ConfigProject.has_section("Ignore"): return []
        if not self.ConfigProject.options("Ignore"): return []
        return [self.ConfigProject.get("Ignore", option) for option in self.ConfigProject.options("Ignore")]


    #----------------------------------------------------------------------
    def get_files_from_project(self):
        """"""
        if not self.ConfigProject.has_section("Files"): return {}
        if not self.ConfigProject.options("Files"): return {}
        return {self.ConfigProject.get("Files", option):bool(int(self.ConfigProject.get("Files", "{}_checked".format(option))))
                for option in filter(lambda f:not f.endswith("_checked"), self.ConfigProject.options("Files"))}


    #----------------------------------------------------------------------
    def get_inherits_from_project(self):
        """"""
        if not self.ConfigProject.has_section("Inherits"): return {}
        if not self.ConfigProject.options("Inherits"): return {}
        return {self.ConfigProject.get("Inherits", option):bool(int(self.ConfigProject.get("Inherits", "{}_checked".format(option))))
                for option in filter(lambda f:not f.endswith("_checked"), self.ConfigProject.options("Inherits"))}


    #----------------------------------------------------------------------
    def get_files_option_from_project(self):
        """"""
        if not self.ConfigProject.has_section("Files"): return {}
        if not self.ConfigProject.options("Files"): return {}
        return {self.ConfigProject.get("Files", option):option
                for option in filter(lambda f:not f.endswith("_checked"), self.ConfigProject.options("Files"))}


    #----------------------------------------------------------------------
    def get_inherits_option_from_project(self):
        """"""
        if not self.ConfigProject.has_section("Inherits"): return {}
        if not self.ConfigProject.options("Inherits"): return {}
        return {self.ConfigProject.get("Inherits", option):option
                for option in filter(lambda f:not f.endswith("_checked"), self.ConfigProject.options("Inherits"))}



    #----------------------------------------------------------------------
    def update_check_status(self, item, int_):
        """"""
        status = item.checkState(int_)
        if status: status = "1"
        else: status = "0"

        if hasattr(item, "path"):

            path = item.path

            inherits = self.get_inherits_option_from_project()
            if path in inherits:
                self.ConfigProject.set("Inherits", inherits[path]+"_checked", status)

            files = self.get_files_option_from_project()
            if path in files:
                self.ConfigProject.set("Files", files[path]+"_checked", status)

            self.save_project(silent=True)



    #----------------------------------------------------------------------
    def close_project(self):
        """"""
        name = self.get_project_name()
        self.project_saved = False
        self.main.treeWidget_projects.clear()
        self.update_project_status("")
        logging.debug("Closing \"{}\" project.".format(name))


    #----------------------------------------------------------------------
    def add_new_file(self):
        """"""
        path = self.get_current_item().path
        if os.path.isfile(path):
            path = os.path.dirname(self.get_current_item().path)

        filename = Dialogs.get_text(self, "New file", default=self.get_untitled_name(ext=".pde")[:-1])
        new_file = os.path.join(path, filename)
        nf = open(new_file, "w")
        nf.close()

        if self.get_current_item().path in self.get_files_option_from_project():
            self.add_existing_file(new_file)

        self.reload_project()

    #----------------------------------------------------------------------
    def add_new_blocks_file(self):
        """"""
        path = self.get_current_item().path
        if os.path.isfile(path):
            path = os.path.dirname(self.get_current_item().path)


        filename = Dialogs.get_text(self, "New blocks file", default=self.get_untitled_name(ext=".gpde")[:-1])
        new_file = os.path.join(path, filename)
        nf = open(new_file, "w")
        nf.close()

        if self.get_current_item().path in self.get_files_option_from_project():
            self.add_existing_file(new_file)

        self.reload_project()


    #----------------------------------------------------------------------
    def add_new_directory(self):
        """"""
        path = self.get_current_item().path
        if os.path.isfile(path):
            path = os.path.dirname(self.get_current_item().path)

        dirname = Dialogs.get_text(self, "New directory", default="untitled-dir")
        new_dir = os.path.join(path, dirname)
        os.mkdir(new_dir)

        if self.get_current_item().path in self.get_files_option_from_project():
            self.add_existing_directory(new_dir)

        self.reload_project()


    #----------------------------------------------------------------------
    def rename(self):
        """"""
        path = self.get_current_item().path
        name = Dialogs.get_text(self, "New name", default=os.path.basename(self.get_current_item().path))
        new_name = os.path.join(os.path.dirname(self.get_current_item().path), name)
        files = self.get_files_option_from_project()
        os.rename(path, new_name)

        if path in files:
            self.ConfigProject.set("Files", files[path], new_name)

        self.reload_project()


    #----------------------------------------------------------------------
    def update_recents_projects(self, filename):

        if filename in self.recent_projects:
            self.recent_projects.remove(filename)
        self.recent_projects.insert(0, filename)
        self.recent_projects = self.recent_projects[:10]

        self.update_recents_menu_project()


    #----------------------------------------------------------------------
    def update_recents_menu_project(self):

        self.main.menuRecentProjects.clear()
        for file_ in self.recent_projects:
            action = QtGui.QAction(self)
            filename = os.path.split(file_)[1]

            len_ = 40
            if len(file_) > len_:
                file_path_1 = file_[:int(len_/2)]
                file_path_2 = file_[int(-len_/2):]
                file_path = file_path_1 + "..." + file_path_2
            else: file_path = file_

            if os.path.isfile(file_):
                action.setText(filename+" ("+file_path+")")
                self.connect(action, QtCore.SIGNAL("triggered()"), self.ide_menu_recent_event(file_))
                action.ActionEvent = self.ide_menu_recent_event

                self.main.menuRecentProjects.addAction(action)

        self.main.menuRecentProjects.addSeparator()
        self.main.menuRecentProjects.addAction(QtGui.QApplication.translate("Dialogs", "Clear recent files"), self.clear_recents_projects)


    #----------------------------------------------------------------------
    def clear_recents_projects(self):

        self.main.menuRecentProjects.clear()
        self.main.menuRecentProjects.addSeparator()
        self.main.menuRecentProjects.addAction(QtGui.QApplication.translate("Dialogs", "Clear recent files"), self.clear_recents_projects)
        self.recent_projects = []



    #----------------------------------------------------------------------
    @Decorator.show_tab("Project")
    def new_library(self):
        """"""
        self.project_saved = False
        self.ConfigProject = RawConfigParser()
        library_name = self.set_project_name(library=True)

        if library_name:
            # add_dir = Dialogs.confirm_message(self, QtGui.QApplication.translate("Dialogs", "Do you want add an existing directory now?"))
            Dialogs.info_message(self, QtGui.QApplication.translate("Dialogs", "Select directory for store your new library."))
            # target_dir = self.select_existing_directory()


            target_dir = Dialogs.set_open_dir(self)

            if target_dir:
                # self.update_project_status(library_name)
                self.create_library_template(target_dir, library_name)
            else:
                self.close_project()

            self.add_existing_directory(os.path.join(target_dir, library_name), inherits_status=True)
            self.update_project_status(library_name)
            self.reload_project()


    #----------------------------------------------------------------------
    def create_library_template(self, target_dir, library_name):
        """"""
        library_dir = os.path.join(target_dir, library_name)
        self.lib = os.path.join(target_dir, library_name, "{}.lib".format(library_name.lower()))

        os.mkdir(library_dir)
        self.add_existing_directory(library_dir, inherits_status=True)
        lib_file = open(self.lib, mode="w")
        lib_file.close()

        self.ide_open_file_from_path(filename=self.lib)



    #----------------------------------------------------------------------
    def compile_library(self):
        """"""
        files = self.get_project_files()

        lib_name = self.get_project_name()

        define = self.lib.replace(".lib", ".h")
        userc = self.lib.replace(".lib", ".c")
        pdl = self.lib.replace(".lib", ".pdl")

        self.pinguinoAPI.preprocess([self.lib], define_output=define, userc_output=userc)


        userc_file = open(userc, mode="r")
        userc_content = userc_file.readlines()
        userc_file.close()

        include = "#include <{}.h>\n\n".format(lib_name)


        functions = self.get_functions()

        pdl_content = []
        for function in functions:
            if function["return"].startswith("PUBLIC"):
                userc_content[function["line"]-1] = userc_content[function["line"]-1].replace("PUBLIC ", "", 1)
                userc_content[function["line"]-1] = userc_content[function["line"]-1].replace(function["name"], "{}_{}".format(lib_name, function["name"]), 1)
                pdl_content.append("{} {}#include <{}.c>".format("{}_{}".format(lib_name, function["name"]), "{}.{}".format(lib_name, function["name"]), lib_name.lower()))
            else:
                userc_content[function["line"]-1] = userc_content[function["line"]-1].replace(function["name"], "{}_{}".format(lib_name, function["name"]), 1)


        userc_file = open(userc, mode="w")
        userc_file.writelines([include] + userc_content)
        userc_file.close()


        pdl_file = open(pdl, mode="w")
        pdl_file.writelines(pdl_content)
        pdl_file.close()






        self.reload_project()




