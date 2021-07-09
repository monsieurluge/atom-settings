import sublime_plugin

class MoveTabCommand(sublime_plugin.WindowCommand):
    def run(self, backward=False):
        window = self.window
        active_view = window.active_view()
        group, view_index = window.get_view_index(active_view)
        if view_index == -1:
            print("no view found")
            return
        print("you are in group " + str(group))
