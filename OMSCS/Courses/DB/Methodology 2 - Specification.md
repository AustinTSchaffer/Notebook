---
tags:
  - OMSCS
  - DB
---
# Methodology 2 - Specification
Ref: [[GTPEgtonline_description.pdf]]
## Login Screen and Registration Screen (Example)
> Requirement: All **Users** are uniquely identified by their **Email Address**. Providing a valid **Email Address** and **Password** combination will log the user into the system.

![[Pasted image 20250917212348.png]]

## Use Attribute Names
- Use the attribute names from the documents in the EER diagram.
- We want the EER diagram to become a high quality model of reality.

![[Pasted image 20250917212813.png]]

![[Pasted image 20250917212800.png]]

## Users vs Admins (Example)
> Requirement: All **Users** (except **Admin Users**) have a profile containing basic information about them.

![[Pasted image 20250917212915.png]]

> Requirement: Admin users have some of the same information as regular users (\[fields listed here\]), but do not have a full profile and cannot request friends. A user must be either an admin or a regular user, but never both. Admin users also record the datetime that they were last logged in to the system.

## Education Section of a User Profile (Example)
> Requirement: A list of **Schools** from which the user can select, is maintained in the system. Assume that all **School Names** will be unique. A user can have any number of schools associated with their profile, and can provide a **Graduation Date** for each school. It is possible that the same school will appear multiple times with different graduation dates.

![[Pasted image 20250917213115.png]]

![[Pasted image 20250917213131.png]]

> Requirement: Each school must have a **School Type**. There are 4 possible types \[listed here\]. It should be possible for the DB admin to add new school types from behind the scenes.

![[Pasted image 20250917213919.png]]

![[Pasted image 20250917213929.png]]

## Professional History of a User Profile (Example)
> Requirement: Admins are responsible for managing the list of **Employers**. Assume that all Employers have a unique **Name**.

![[Pasted image 20250917214625.png]]

> Requirement: The **Job Title** field is not managed by the administrator and can be any value provided by the user. A profile can contain multiple **Employers** and the same **Employer** may even appear multiple times as long as the **Job Title** is different in each case.

![[Pasted image 20250917214728.png]]

## Friendship (Example)
> Requirement: **Friendship** is not always reciprocal. Just because Emily is friends with Sarah, this does not imply that Sarah is friends with Emily. The **DateConnected** field is set when the friend request is accepted, not when the request is originally sent.

![[Pasted image 20250917214858.png]]

## EER Diagram (Example)
![[Pasted image 20250917214925.png]]

![[Pasted image 20250917215129.png]]

## Data Formats - beg, steal, borrow
![[Pasted image 20250917215222.png]]

User
- Email: max 36 characters
- Password: max 20 characters
- Name:
	- FirstName: max 25 characters
	- LastName: max 40 characters
- Addresses (when needed) are very very difficult (USPS Publication 28: https://pe.usps.com/text/pub28/welcome.htm)

Regular User
- Birthdate: Date
- Sex: {M, F}
- Current City, Home Town: max 20 chars each
- Interests: multi-value with 16 characters each

Beg, Steal, Borrow: If someone has already spent a lot of time developing a specific data format, why would you replicate that work to create something bespoke?

## Constraints
Examples:
- Date Connected is NULL until request is accepted.
- Cannot be Friend with yourself.
- Users can only comment on Status of Friends.

Already Covered, i.e. DON'T include these when enumerating constraints of the application.
- Data formatting constraints
- Constraints that can be expressed in the EER Diagram

These are constraints that cannot be (easily) programmed into the schema of the database, and therefore must be encoded/handled by the software application.

## Task Decomposition
- Look at each task in the IFD. Is that task a single task, or can it be broken down into multiple tasks?
- Rules of thumb
	- Lookup vs modify (insert, delete, and/or update)? (different database locks)
	- How many schema constructs are involved? (many database locks)
	- Are enabling conditions consistent across tasks? (let run what can run - scheduling)
	- Are frequencies consistent across tasks? (index only what must be indexed)
	- Is consistency essential?
		- ACID transaction properties
		- Bank transfer requires high consistency, for example
	- Is mother task control needed or not?

## Web Apps vs Traditional Apps
- Web apps
	- Traditionally, almost stateless
	- must have some state (e.g. login sessions)
	- May need some click stream history.
	- Web 2.0 and AJAX technologies provide more rich user interface in Web browser.
- Traditional apps
	- in a traditional app, it is much easier to manage local state separately from the DB
	- a whole slew of changes can be collected before submitting them all to the DB
	- Supports better control of ACID transaction execution

## View Profile Task Decomposition (Example)
View Profile
- three lookups for a Regular User
	- Personal Information
	- Education Information
	- Professional Information
- all three are
	- read-only
	- enabled by a user's login or a friend's lookup
	- same frequency
- several different schema constructs are needed
- consistency is not critical, even if the profile is being edited by the user while a friend is looking at it
- They can be done in any order
- all three must be done in order to display the View Profile view, so a mother task is needed.
- Should be decomposed into 3 sub tasks.

![[Pasted image 20250917220858.png]]

**View Profile - Abstract Code**
- Find the current User, using the User Email
- Display User Name
- Find the current RegularUser using the User Email
- Display RegularUser Sex, Birthdate, CurrentCity, Hometown, and Interests
- Find each School for the Regular User
	- Display SchoolName and YearsGraduated
	- Find SchoolType
	- Display SchoolType Name
- Find each Employer for the RegularUser
	- Display Employer Name and JobTitles

![[Pasted image 20250917221129.png]]

## Edit Profile Task Decomposition (Example)
- Lookups of Personal, Education, and Professional information of a Regular User (use: **View Profile** task)
- Lookups of School and Employer lists
- Edits of Personal, Education, and Professional information
- Read, insert, delete, and update
- All three are enabled by a user's login and separate edit request
- Different frequencies (in which fields are edited)
- Several different schema constructs are needed
- Consistency is not critical, even if the profile is being looked at by a friend of the user
- Lookup done first followed by any number of edits and lookups
- Mother task is needed
- **Must be decomposed into sub tasks**

![[Pasted image 20250917222356.png]]

![[Pasted image 20250917222445.png]]

## Task Decomp Friend Requests etc.
![[Pasted image 20250917222518.png]]










