# EF Core

Talk By: https://letyournerdbeheard.com/

## Code First vs DB First

- Code First
    - Code becomes the keeper of the schema
    - Schema is versioned with the code
    - Errors at Design Time
- Database First
    - DB is the keeper of the schems
    - Schema is versioned outside of the code
    - Errors at runtime (`SET ANSI_NULLS ON`)

## Picking Code First or DB First?

It is possible to retrofit Code First onto DB First

## Software Needed 

- .NET Core 2.2 SDK
- Windows?
  - VS2017 15.7 or later
  - Buncha other stuff
- !Windows?
  - VSCode with C# Extension

## Useful Commands

```bash
dotnet new etc
dotnet ef migrations add [MigrationName] -o EntityFramework/Migrations
dotnet ef database update
```

## Cool Ideas

- Versioned DB schemas
- Container images for DB Schemas
    - Issue/Question: Permissions and credentials?
- All defined in C# POCOs (Models): Indexes/FK Relations/Constraints/Etc
- DB Controlled/Defined by Class/Property attributes
- Object inheritance defined by C# interhitance
- Connectors to arbitrary DB vendors
    - http://www.npgsql.org/
    - https://dev.mysql.com/doc/connector-net/en/connector-net-entityframework-core-example.html
- Easy Swagger Integration
- Repository Patterns (https://codingblast.com/entity-framework-core-generic-repository/)
- Override `SaveChanges` on DbContext to provide auto-auditing
    - Put "createdby" "changedby" "createddate" and "changeddate" in the base
      model
- For EF Model <-> API ViewModel, use AutoMapper
    - (`AutoMapperProfile.cs`)
    - (`services.AddAutoMapper(typeof(AutoMapper))`)
- Add `IsDeleted` to base model for "Soft Deletes"
    - Add Global Query Filter to exclude entities where "IsDeleted"
    - (Danger<Sucks>: Getting all deleted items after configuring this)

## Things to Consider

- `[ProducesResponseType]` is for documentation
- EF is already a Unit Of Work pattern, so avoid putting a Unit Of Work pattern
  on top of it
- Use `async` for all WebApi junk
- `ICurrentUserService` 🤷‍♂
- VStudio still sucks at not locking things

