#!/bin/sh
checkroot() {

if [[ "$(id -u)" -ne 0 ]]; then
   printf "\e[1;77mPlease, run this program as root!\n\e[0m"
   exit 1
fi
}

while :
 do
    clear
                  figlet -w 200 -f "poison" "Meta"
                  date '+%d %B %Y %T' | toilet -f term -F border | lolcat
                  echo "\033[0;32m------------------------------------------------------------------------------"
                  echo "    Meta embeds a base64 encoded string into an image                                   "
                  echo "    Meta can decode the base64 encoded string revealing the hidden message              "
                  echo "    This tool uses Python3                                                              "
                  echo "\033[0;32m------------------------------------------------------------------------------"
                  echo "\033[01;33m[1]  Encode" | lolcat
                  echo "\033[01;32m[2]  Decode" | lolcat
                  echo "\033[01;31m[0]  Exit"
                  echo "\033[01;31m=====================================================================\033[0m"
                  echo "\033[01;37m Enter your choice [1-24]:\033[0m "

    read choice


    case $choice in
      1) cd ~/Projects/meta && python3 metadata.py; echo "Press any key" | lolcat; read;;
      2) cd ~/Projects/meta && python3 metareader.py; echo "Press any key" | lolcat; read;;


      0) exit 0 ;;
      *) echo "Oops!!! 😜  Please select a correct choice" | lolcat;
         echo "\033[01;33m Press any key" | lolcat ; read ;;
 esac
done
