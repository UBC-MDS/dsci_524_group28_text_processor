# Contributing

Contributions of all kinds are welcome here, and they are greatly appreciated!
Every little bit helps, and credit will always be given.

## Example Contributions

You can contribute in many ways, for example:

* [Report bugs](#report-bugs)
* [Fix Bugs](#fix-bugs)
* [Implement Features](#implement-features)
* [Write Documentation](#write-documentation)
* [Submit Feedback](#submit-feedback)

### Report Bugs

Report bugs at [here](https://github.com/UBC-MDS/dsci_524_group28_text_processor/issues).

**If you are reporting a bug, please follow the template guidelines. The more
detailed your report, the easier and thus faster we can help you.**

### Fix Bugs

Look through the GitHub issues for bugs. Anything labelled with `bug` and
`help wanted` is open to whoever wants to implement it. When you decide to work on such
an issue, please assign yourself to it and add a comment that you'll be working on that,
too. If you see another issue without the `help wanted` label, just post a comment, the
maintainers are usually happy for any support that they can get.

### Implement Features

Look through the GitHub issues for features. Anything labelled with
`enhancement` and `help wanted` is open to whoever wants to implement it. As
for [fixing bugs](#fix-bugs), please assign yourself to the issue and add a comment that
you'll be working on that, too. If another enhancement catches your fancy, but it
doesn't have the `help wanted` label, just post a comment, the maintainers are usually
happy for any support that they can get.

### Write Documentation

Text Processor could always use more documentation, whether as
part of the official documentation, in docstrings, or even on the web in blog
posts, articles, and such. Just
[open an issue](https://github.com/UBC-MDS/dsci_524_group28_text_processor/issues)
to let us know what you will be working on so that we can provide you with guidance.

### Submit Feedback

The best way to send feedback is to file an issue at
[here](https://github.com/UBC-MDS/dsci_524_group28_text_processor/issues). If your feedback fits the format of one of
the issue templates, please use that. Remember that this is a volunteer-driven
project and everybody has limited time.

## Git Workflow

We use **GitHub Flow** - industry-standard contribution workflow:

1. Fork the repository on GitHub:
   https://github.com/UBC-MDS/dsci_524_group28_text_processor
   
2. Clone your fork locally (*if you want to work locally*)

    ```shell
    git clone git@github.com:your_name_here/dsci_524_group28_text_processo.git
    ```

3. [Install hatch](https://hatch.pypa.io/latest/install/).

4. Create a branch for local development using the default branch (typically `main`) as a starting point. Use `fix` or `feat` as a prefix for your branch name.

   Our branch name recommendation: <type>/<short-purpose>-<author>
      
      type = fix, feat, docs
      
      short-purpose = purpose of the change
      
      author = your GitHub username
   
   Example: docs/update-contributing-guide-vtphan

   Then run:

    ```shell
    git checkout main
    git checkout -b fix-name-of-your-bugfix
    ```

    Now you can make your changes locally.


5. When you're done making changes, apply the quality assurance tools and check
   that your changes pass our test suite. This is all included with tox

    ```shell
    hatch run test:run
    ```

6. Commit your changes and push your branch to GitHub. 

   Keep commits small and meaningful.
   
   Use semantic commit messages (https://www.conventionalcommits.org/).

    ```shell
    git add .
    git commit -m "fix: summarize your changes"
    git push -u origin fix-name-of-your-bugfix
    ```

7. Open the link displayed in the message when pushing your new branch in order
   to submit a pull request.

### Pull Request Guidelines

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.
2. If the pull request adds functionality, the docs should be updated. Put your
   new functionality into a function with a docstring.
3. Your pull request will automatically be checked by the full test suite.
   It needs to pass all of them before it can be considered for merging.

### Merge Rules

1. Only maintainers can merge Pull Request
2. A PR can only be merged when:
   - At least 1 approving review is given
   - All requested changes are resolved
3. The contributor branch will be deleted after merge
4. Force-pushing is not allowed after a PR is opened unless requested by a maintainer
