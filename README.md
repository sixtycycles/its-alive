its-alive
simple "its alive" check in from remote office to cloud/other office. 


# remote server #
the remote server can be a vps, or someones house. There is a wireguard tunnel setup between the remote and campus system, to allow it to bypass NAT at someone's house. 

the remote server has  `~/scripts` folder
which contains an empty file `last_check` and `notify_if_dead.py` as well as `sign the book.py` the latter is called by the remote system checking in, which writes a timestamp to a file. 

`notify_if_dead` should be set to run like so: 

### crontab ###

`* * * * * /usr/bin/python3 /home/USERNAME/scripts/notify_if_dead.py`

# Campus server #

this server's only job is to run `still_here.py` to ssh over the wireguard tunnel to the remote host, and execute "sign the book" to timestamp the file. this serves as an indicator that someone is alive at work, and you dont have to drive down there to check it out. 

so, only notify if the remote server hasn't heard from campus in more than x minutes. 
