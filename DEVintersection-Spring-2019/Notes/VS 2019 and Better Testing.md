# VS 2019 and Better Testing

- VS 2019 has had performance enhancements
- Faster branch switching
- memory consumption reduction by test processes, faster test discovery
- Switched from assembly-based test discovery to source-based

## New Test Explorer UI

- mem improvements
- persisted test explorer data
- filter buttons
- customizable test hierarchy
- additional buttons for running
- improved test status pane
- playlists tab
- configurable columns
- etc

> Try docking horizontally!

- group tests by: project, class, state, duration, namespace, target framework, etc (any order)
- fixed width font in test status pane, better text highlighting
- better test playlists (they (can) open in a separate tab)
- you can start "live unit testing" from Test Explorer
- excluding tests from "live unit testing" (right clicks in some places)
- `TestCategory` for skipping live unit testing (test method attribute)

> Roslyn: 50% OSS Contributions, 4 million lines of code, thousands of tests.

## Types of Tests

There's a general perscribed pyramid hierarchy to describe how many of what kinds of tests you should write and run:

- Most should be unit tests
- Fewer should be integration tests
- Fewer should be acceptance tests
- Fewest should be UI tests (Visual Studio has 0 ZERO NONE UI tests)
- Tangental tests
  - Load and performance tests
  - Acceptance (business desired outcome)
  - Exploratory/Manual tests

CUIT are deprecated. Sounds like that statement is a "full stop" situation to me.
Mentioned how they never really game the MSoft teams useful results.
MSoft is pushing people toward selenium and appium tests.

> TDD is writing a failing test then writitng the code to make it pass. Points out things that are not isolated.

## Smart Testing

- generate test method stubs. RIGHT CLICK AND CREATE UNIT TEST. (.net framework only)
- analyze code coverage (runs at DLL level) (integrates with AZ DO pipes)
- intellitest

Intellitest is Enterprise only. (.net FW and C# only)
Right click, intellitest context menu. R.C.&Run intellitest to generate the tests.

Code fix to sync namespace names between the project and test project.
