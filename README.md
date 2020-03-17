# Database application: Bug reports and feature requests

[View a live demo](https://tsoha-2020-bugtracker.herokuapp.com/)

Even though there exists a myriad of bug trackers and feature request systems,
including the current home of this project itself (Github), I've decided to
implement one as an excercise.

The application will have user registration and login, user roles (developer
and user for now), projects which the reports will concern, reports with types
(bug/request), progress-statuses and priorities, keyword-tags for the reports
and basic listing/search which can be sorted by priority, progress and/or age.

## Database diagram

![Database diagram](documentation/database_diagram.png)

The main object here is the Report. All Reports have been reported by an user
at some time, have a priority (arbitrarily chosen from 0 which means won't fix
to 10 which means critical), have a progress (again, arbitrarily 0 means not
started, 10 means done), can have tags, and concern only some Project.

For the sake of simplicity and to encourage everyone to have a try, I've chosen
not to have assignees for Reports.
