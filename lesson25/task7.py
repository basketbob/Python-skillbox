class TaskManager:
    lifo = []

    def __str__(self):
        return 'here TaskManager!'

    def new_task(self, name, priority):
        pass

    def add_elem(self, elem):
        self.lifo.append(elem)

    def remove_elem(self, elem):
        self.lifo.remove(elem)


manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать дз", 2)
print(manager)
