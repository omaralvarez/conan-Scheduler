from conans import ConanFile, CMake, tools
import os


class SchedulerConan(ConanFile):
    name = "Scheduler"
    version = "master"
    description = "Modern C++ Scheduling Library https://github.com/omaralvarez/Scheduler"
    license = "MIT"
    url = "https://github.com/omaralvarez/conan-Scheduler"
    repo_url = "https://github.com/omaralvarez/Scheduler"
    author = "Bosma, Omar Alvarez"
    requires = "CTPL/0.0.2@omaralvarez/public-conan"
    no_copy_source = True

    def source(self):
        self.run_command("git clone %s" % (self.repo_url))
    
    def run_command(self, cmd, cwd=None):
        self.output.info(cmd)
        self.run(cmd, True, cwd)

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="Scheduler")
        cmake.install()

    def package_id(self):
        self.info.header_only()
