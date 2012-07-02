#!/usr/bin/env python

import todolist.model
todolist.model.db.create_all()

task = todolist.model.Task("Finish this todolist application.")
todolist.model.add(task)
todolist.model.save_all()

print "Created the todolist database"
