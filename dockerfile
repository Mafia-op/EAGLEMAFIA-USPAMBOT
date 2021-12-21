_get_repolink () {
    local regex
    regex='(https?)://github.com/.+/.+'
    if [[ $EAGLE_REPO == "EAGLEYUVI SPAMUSERBOT" ]]
    then
        echo "aHR0cHM6Ly9naXRodWIuY29tL1RlYW0tTWFmaWEvc3BhbWJvdC9hcmNoaXZlL21hc3Rlci56aXA=" | base64 -d
    elif [[ $EAGLE_REPO == "EAGLEYUVI SPAMUSERBOT" ]]
    then
        echo "aHR0cHM6Ly9naXRodWIuY29tL1RlYW0tTWFmaWEvc3BhbWJvdC9hcmNoaXZlL21hc3Rlci56aXA=" | base64 -d
    elif [[ $EAGLE_REPO =~ $regex ]]
    then
        if [[ $EAGLE_REPO_BRANCH ]]
        then
            echo "${EAGLE_REPO}/archive/${EAGLE_REPO_BRANCH}.zip"
        else
            echo "${EAGLE_REPO}/archive/master.zip"
        fi
    else
        echo "aHR0cHM6Ly9naXRodWIuY29tL1RlYW0tTWFmaWEvc3BhbWJvdC9hcmNoaXZlL21hc3Rlci56aXA=" | base64 -d
    fi
}


_set_bot () {
    local zippath
    zippath="EAGLEYUVI SPAMUSERBOT.zip"
    echo "  Downloading eagleyuvi spamuserbot  Source Code..."
    wget -q $(_get_repolink) -O "$zippath"
    echo "  Unpacking Data ..."
    EAGLEPATH=$(zipinfo -1 "$zippath" | grep -v "/.");
    unzip -qq "$zippath"
    echo "Done"
    echo "  eagleyuvispamuserbot  Cleaning.."
    rm -rf "$zippath"
    sleep 5
    cd $EAGLEPATH
    echo "    🐍 ֆȶǟʀȶɨռɢ ֆʍօȶɦɛֆ ɛǟɢʟɛʏʊʋɨֆքǟʍʊֆɛʀɮօȶ 🐍     "
    echo "
    EAGLEYUVI SPAMUSERBOT
    "

    python3 ../setup/updater.py ../requirements.txt requirements.txt
    python3 -m userbot
}

_set_bot









