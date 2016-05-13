#!/bin/bash

# works with a file called VERSION in the current directory,
# the contents of which should be a semantic version number
# such as "1.2.3"

# this script will display the current version, automatically
# suggest a "minor" version update, and ask for input to use
# the suggestion, or a newly entered value.

# once the new version number is determined, the script will
# pull a list of CHANGELOG.MD from git history, prepend this to
# a file called CHANGELOG.MD (under the title of the new version
# number) and create a GIT tag.

today=$(date +"%F %R")

if [ -f VERSION ]; then
    BASE_STRING=`cat VERSION`
    BASE_LIST=(`echo $BASE_STRING | tr '.' ' '`)
    V_MAJOR=${BASE_LIST[0]}
    V_MINOR=${BASE_LIST[1]}
    V_PATCH=${BASE_LIST[2]}
    echo "Current version : $BASE_STRING"
    V_MINOR=$((V_MINOR + 1))
    V_PATCH=0
    SUGGESTED_VERSION="$V_MAJOR.$V_MINOR.$V_PATCH"
    read -p "Enter a version number [$SUGGESTED_VERSION]: " INPUT_STRING
    if [ "$INPUT_STRING" = "" ]; then
        INPUT_STRING=$SUGGESTED_VERSION
    fi
    echo "Will set new version to be $INPUT_STRING"
    echo $INPUT_STRING > VERSION
    
    echo "## Version $INPUT_STRING [$today]:" > tmpfile    
    echo "" >> tmpfile
    git log --pretty=format:" - %s" "v$BASE_STRING"...HEAD >> tmpfile
    echo "" >> tmpfile
    echo "" >> tmpfile
    echo "" >> tmpfile
    cat CHANGELOG.MD >> tmpfile
    mv tmpfile CHANGELOG.MD
    git add CHANGELOG.MD VERSION
    git commit -m "Version bump to $INPUT_STRING"
    git tag -a -m "Tagging version $INPUT_STRING" "v$INPUT_STRING"
    git push origin --tags
else
    echo "Could not find a VERSION file"
    read -p "Do you want to create a version file and start from scratch? [y]" RESPONSE
    if [ "$RESPONSE" = "" ]; then RESPONSE="y"; fi
    if [ "$RESPONSE" = "Y" ]; then RESPONSE="y"; fi
    if [ "$RESPONSE" = "Yes" ]; then RESPONSE="y"; fi
    if [ "$RESPONSE" = "yes" ]; then RESPONSE="y"; fi
    if [ "$RESPONSE" = "YES" ]; then RESPONSE="y"; fi
    if [ "$RESPONSE" = "y" ]; then
        echo "0.1.0" > VERSION
        echo "Version 0.1.0" > CHANGELOG.MD
        git log --pretty=format:" - %s" >> CHANGELOG.MD
        echo "" >> CHANGELOG.MD
        echo "" >> CHANGELOG.MD
        git add VERSION CHANGELOG.MD
        git commit -m "Added VERSION and CHANGELOG.MD files, Version bump to v0.1.0"
        git tag -a -m "Tagging version 0.1.0" "v0.1.0"
        git push origin --tags
    fi

fi