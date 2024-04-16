# Changing commit names
Change commit names is simple, You can use the `emmet` command to do wo in the last commit, if you just issued a commit with a wrong name and commit message. The whole command follows ahead:

```bash
git commit --amend -m "New commit message."
```

If you want to bulk change a big number of names, you can use the following command:

```bash
git rebase -i HEAD~X  
```

By doing that you will be presented with a list with the last `X` commits, like `3` or `40`, and you can read the instructions and mark the files that you want to change the name. Then the default git editor will open for each entry.

Remember, by changing the name of the commits you are changing the commit as well, so it will change all the following commits. Be carefull by pushing these modifications to the cloud if the commits changed involve third party modifications. This is dangerous, so much so that you need to issue a `git push --force` to send the modified commits and the commits that were substituted will no longer exist. They will have the same code and modifications but the references will be rebuild.

Perform these type of operations with caution.

