# Reflection: Tools, Infrastructure, and Practices

During the development of text_processor, we utilized a collaborative software development workflow that focused on building and maintaining a software package for use by others. Specifically we used GitHub Flow to manage our development and implemented main branch protection to ensure all code was reviewed before merging into main. We also utilized the GitHub project board and issue tracking to maintain accountability and visibility within our team.

Our documentation pipeline leveraged quartodoc to automatically generate the API reference pages directly from our docstrings, ensuring that the documentation would always synchronize with code changes. We used Quarto to render the website and GitHub pages for public hosting. To manage the software life cycle, we implemented continuous integration (CI) through GitHub Actions. This infrastructure handled the quality control by automatically running the pytest suite and using Ruff for code linting and formatting.

We analyzed our GitHub project insights to evaluate our team's velocity and workload contributions over the 4 milestones of this software development. The burn up chart shows that there was an increase in requirements for milestones 2 and 4, coinciding with the heavy development phases of the project. Note: milestone 4 includes cleanup and addressing peer reviews from TAs and fellow classmates which created a bottleneck at the end of the software completion. Burn up by status confirms our highest velocity period was during milestone 2 with 18 completed tasks, which is more than double the tasks of milestone 1 and milestone 3. In terms of workload and contributions, the Burn up by assignee demonstrates that there was a relatively balanced effort across the team.

# DAKI Analysis (Drop, Add, Keep, Improve)

Reflecting on our workflows using the DAKI framework, we have identified the following:

-   Drop: We would drop the reliance on manual versioning and move towards the automated tagging to reduce overhead

-   Add: We would implement standardized Issue Templates with a mandatory "Definition of Done" checklist. This will ensure that the reviewer will only recieve code that meets our quality standards.

-   Keep: We would keep the usage of the centralized project task board for visibility and accountability for the team.

-   Improve: Separating tasks into smaller sub-issues to help track progress more accurately

# Scaling the Project

If we were to scale text_processor, we would implement the following:

-   Containerization: we would transition to a containerized infrastructure eg Docker to simplify cross platform deployments for our users.

-   Expand test matrix: We would extend the CI testing to run across a matrix of multiple Python versions (3.10, 3.11, and 3.12) and operating systems to ensure compatibility for all users.

-   Transition to Git Flow: To manage more complex releases, we would move from GitHub Flow to Git Flow. In this setup, new features would be developed on separate branches and merged into a dedicated develop branch, and only after the code has been thoroughly tested and reviewed is it officially released onto the main branch. This structure ensures that only well tested and stable code reaches the production environment.

-   Implementation of CODEOWNERS: To manage the growing contributor base, we would implement a CODEOWNER file. This would allow automated assignment to specific reviewers for pull requests based on files being modified. This will ensure that domain experts will always oversee the changes to the codebase.