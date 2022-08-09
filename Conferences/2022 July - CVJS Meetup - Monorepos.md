# CVJS Meetup - Monorepos

July 27, 2022

> Webcomponents are contentious apparently.

## Terms

- Monolith
	- /app
	- /app/lib
- Monorepo
	- /app
	- /app2
	- /lib
- Polyrepo
	- Like monorepo but in seperate repos

One of the big questions is what happens when one of the dependencies needs to get updated. Biggest difference between mono- and poly- repo is what happens when you need tp update /lib or a dependency of /lib. For Polyrepo, it's possible for different apps to reference different versions of /lib, which becomes a problem for cognitive load.

The biggest advantage of monorepo is making sure that each commit of the project makes sense in the context of the single repository. You don't need multiple PRs. You don't need to go look at different repos every time something is broken.

## AntiPatterns
- Versioning your monorepo packages as if they're a polyrepo
	- Instead of referencing the local code files, it references a private NPM package.
	- Issue: If you check out your code base, finding the code you're running is just like looking for code in the polyrepo pattern, except worse.
- Co-location, each app is independent and code sharing is ctrl+c, ctrl+v.
	- Bad. Don't do.

## Tools
- npm workspaces
- pnpm
- Yarn workspaces
- Nx
- Lerna
- Others...

## Newness

- We used to call these things a "shared codebase"
- Just use `make`?

## JS Workspaces

It's basically yarn/npm creating symlinks in `/node_modules`

`pnpm` also solves this problem but also tries to save space and avoid duplications. It's kind of not needed anymore for new projects.

## Monorepo tools

How do you build the whole repo if build order matters? How do you publish?

How do you only run tests (and deployments) on packages that have changed?

- `turborepo` and `nx` reinvent `make` but with JSON
	- `nx` is pretty opinionated about how builds works. Google uses `nx` internally.
	- `turborepo` is basically brand new and was purchased by Vercel.
- `lerna`
	- unifies scripting tasks.
	- It basically just runs `build` in every sub-project. It's not really optimized for builds, but it's easy to use and a great way to get started.
	- It was basically just one guy who made it and the classic FOSS thing happened, so he tried to abandon the project. Nrwl picked it up and is now maintaining it. They're the same people that do `nx`.
- `rush` is a Microsoft-backed monorepo tool.
	- Automatic dependency graph, incremental builds
	- Enterprisey features, mandatory changelogs,  etc.
- `bas([ie])l` Is Google's enterprise tool.
- Monopack is a ChartIQ/Cosaic tool.

## Monorepo Good?

- Atomic Changes
- Large scale code refactoring
- Developer mobility (easy to onboard someone into a project if it's in the same repo they're already working in)

(Monoliths are also good, it's the same thing.)

## Monorepos Bad?

- Other teams can change your team's code. Need to maintain a CODEOWNERS file.
- How to CI test "just the part that changed". Either your CI tool deeply understands your dep graph (nx/turborepo) or you spend extra time building/testing everything, all the time.
- Security / Auditing
- Long clone/checkout/fetch times. Too many files for one hard drive? IDE dying on open?

## \[DEMO\]
