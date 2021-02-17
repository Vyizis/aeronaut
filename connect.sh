#!/bin/sh
mv irccat.json irccatwith.json
mv irccatwithout.json irccat.json
sleep 10
mv irccat.json irccatwithout.json
mv irccatwith.json irccat.json
