#!/usr/bin/zsh

# Use it as a reminder for daily chores
task add "Go for a workout session at the gym" due:tod recur:P2D project:health
task add "Go for a run" due:tom recur:P2D project:health
task add "Walk my dog" due:tod recur:P1D project:social.dog

# Do chores incrementally
task add "Clean your home" project:housekeeping recur:weekly due:tod
task add "Update dotfiles" project:technical.linux recur:weekly due:tod

# Incremental reading: the core benefit of task-increment
task add "Catch up to my RSS feeds on newsboat and add interesting links to taskwarrior for incremental reading" project:technical due:tod recur:weekly
task add "https://skerritt.blog/set-theory-for-competitive-programming/" project:technical.study
task add "Musashi by Eiji Yoshikawa" project:philosophy.reading
task add "Bertrand Russel's History of Western Philosophy" project:philosophy.reading

# Make incremental progress on tasks that have deadlines
# Tasks with deadlines automatically have a higher priority and therefore have a greater probability of popping up on your task-increment feed
task add "Fix issue #234 in dstask" project:technical.dstask due:sun
task add "Prepare for sourcehut job interview" project:career due:1st
task add "Schedule a one-on-one with client to know next plans and feedback" project:career.freelance.project_medea due:now+9d

# Use it as a reminder for tasks you plan to do eventually but just cannot find the right time to do so
task add "Ask Lydia out on a date" project:social.dating
task add "Call mother" project:social.family recur:monthly due:1st
task add "Delete Instagram" project:privacy
