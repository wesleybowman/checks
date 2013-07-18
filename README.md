checks
======

Job and file checking.


checkRunning
============

A basic checker to see if a job has started running using the qstat command.
All that needs to be changed here is the userInfo.txt. An example of how the
data needs to look is provided in the file. When the job starts, it will then
send a self email to the user. This could be updated for text messaging as well
if desired.

