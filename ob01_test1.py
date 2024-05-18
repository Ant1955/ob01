# Создай класс `Task`, который позволяет управлять задачами (делами).
# У задачи должны быть атрибуты: описание задачи, срок выполнения и статус
# (выполнено/не выполнено). Реализуй функцию для добавления задач,
# отметки выполненных задач и вывода списка текущих (не выполненных) задач.

class Task:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, deadline):
        self.tasks.append({
            'description': description,
            'deadline': deadline,
            'completed': False
        })

    def mark_completed(self, description):
        for task in self.tasks:
            if task['description'] == description:
                task['completed'] = True
                break

    def get_current_tasks(self):
        return [task for task in self.tasks if not task['completed']]

    def get_all_tasks(self):
        return [task for task in self.tasks]

# Пример использования:
task_manager = Task()
task_manager.add_task('Закончить ДЗ', '2024-05-20')
task_manager.add_task('Купить продукты', '2024-05-18')
task_manager.add_task('Ответить про лицнзирование StoreOnce', '2024-05-19')
task_manager.mark_completed('Купить продукты')
current_tasks = task_manager.get_current_tasks()
all_tasks = task_manager.get_all_tasks()
print("Список текущих задач:")
for task in current_tasks:
    print(f"Описание: {task['description']}, Срок: {task['deadline']}, "
          f"Статус: {'Выполнено' if task['completed'] else 'Не выполнено'}")
print(f"Всего задач: {len(all_tasks)}")
print("Все задачи:")
for task in all_tasks:
    print(f"Описание: {task['description']}, Срок: {task['deadline']}, "
          f"Статус: {'Выполнено' if task['completed'] else 'Не выполнено'}")