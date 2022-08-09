---
tags: Conference, dotnet, CSharp
---

# DEVintersection Spring 2019

This section is dedicated to all of the notes that I took while at DEVintersection Spring 2019.

## Talks Attended - Day 1

### Actors - The Past and Future of Software Engineering

**By:** Juval Lowy

> The Actor Model is the latest fad to storm the software industry. But is there any substance behind it and why should you care? What are the drivers of the Actor Model and why have the large cloud vendors started offering Actor-based solutions?
> 
> Juval Lowy puts it all together first by outlining the long-term trend in software methodologies that brought this 50-years old computational model to the fore, and how the demise of Moore's Law coupled with the rise of the IoT  will force us to abandon sequential programming. Juval will examine the origin of the Actor Model; demonstrate Actors using conceptual examples, outline emerging design patterns, point out common misconceptions and conclude with his views on the future of the Actor Model.

As the description states, this talk was mostly conceptual. Not much in the wayof concrete or tangible examples were offered by the content of this talk, but it was an interesting outlook on the history and direction of hardware and software. Still, I felt that this talk was a bit too lofty and head-in-the-clouds for a technical conference, but my colleague really enjoyed it so your mileage may vary I suppose. I was actually kind of amazed how long the talk went on before the term "services" was used, micro or otherwise.

In all honesty, I feel that I got more out of being on Slack during portions of the talk. `cameronstinson4` and I were trying to wrap our minds around the management of our Slack's Factorio server, running on an EC2 VM. We are planning on having some way to start and stop the VM in order to save money. Given that EC2 VMs have dynamic public IPs by default, we ran into a problem with the the IP changing every time the server is restarted. Also, there does not appear to be an easy way to set a public DNS name for an EC2 VM with a dynamic IP address, to the point where we found web services such as [No-IP](https://www.noip.com/) and [Dyn](https://dyn.com/dynamic-dns/). The alternative would be to set up a load balancer or some other routing agent that could access the Factorio server using a local DNS name, via a virtual network in AWS.  

We decided that it would be best to just give the VM a static IP address and call it a day. He then decided to just make the current IP address viewable on his website, along with some server controls.

### Zero to Database with EF Core Code First in 60 minutes

**By:** Justin James

**GitHub:** https://github.com/digitaldrummerj and https://github.com/nerdbeheard

> Finally, you can create a database with just C# that even your DBA would be proud. Never again will you have to wait for the DBA to create the database for you. Plus you will get to version your database schema along with the rest of your code!
>
> With EF Core, everything you need comes right out of the box to quickly define your tables, column attributes, relationships, indexes, plus much more. We will start at the beginning with generating a new project and by the end we will a fully finished database. At the end of this talk you will be able to create your database using EF Core Code First.

This was a practical talk with concrete code examples, all built upon a single demo database. Each section of the talk added something a little more complex o n top of a simple entity relationship, each adding its own DB Migration on top of the previous sections. I really feel like I'm taking something to take home from this one.

EF Core looks like a solid piece of tech. The sample code from the talk has bee n added as a git submodule.

https://github.com/digitaldrummerj/efcore-code-first-demo

### Docker and Kubernetes for Developers

**By:** Dan Wahlin

**GitHub:** https://github.com/DanWahlin

> Docker provides an excellent way to "containerize" applications. Kubernetes is popular open-source system for automating deployment, scaling, and management of containerized applications. Put them together and you can do some pretty phenomenal things. In this session, Dan Wahlin will discuss the role that Docker and Kubernetes plays in the developer workflow, describe key concepts such as pods, nodes, and deployments, and show how you can get started using both today. If you've heard about Docker and Kubernetes but haven't made time to learn more about them then this is the session for you!

Barely scratched Kubernetes. Decent Docker primer though, for anyone who is unfamiliar.

## Talks Attended - Day 2

### Functional Techniques for C#

**By:** Kathleen Dollard

**GitHub:** https://github.com/KathleenDollard

> You are effective with the imperative, object-oriented core of .NET but you look longingly at the winsome smile of functional languages. If you’re interested in your language’s functional features, but aren’t sure how to get it right or take full advantage of them, then this talk is for you. In .NET, functional techniques leverage delegates, lambda expressions, base classes and generics, so the talk starts with some basics. You’ll learn which code to attack with functional ideas and how to do it. You’ll look at code similar to what you write every day and see it transform from long difficult to follow code to short code that’s easy to understand, hard to mess up and straightforward to debug. Functional approaches help you write less code and apply patterns in a clear and consistent way. This talk will help you start or continue your journey with functional techniques in C#.

This talk was incredible. Good code samples. Well presented and well reasoned. Really made a case for designing well structured static methods for business logic. You can review the notes of the talk in the "Notes" directory. I'm not sure how I would go about utilizing what Kathleen presented, but there were a couple of big takeways for me.

1. **Inside-Out** refactoring occurs when you pull a block of code into its own
   method, so you can use a method call instead of copying the code.
   **Outside-In** refactoring occurs in a similar manner, except it occurs when
   the method accepts a function, which allows you to reuse a surrounding code
   block. This is useful in cases where you have a commonly reoccurring code
   block, such as a collection of stacked `using()` statements, or a common
   `try-catch` block.

2. STOP ALLOWING THROWN EXCEPTIONS. Kathleen presented a case for recreating the
   `Option` type in C#, which is a native feature in F#. Kathleen presented an
   alternative naming convention: `FailureResult` and `SuccessResult`, as
   opposed to a direct translation of `None` and `Some`. The advantage of this
   is that it allows you to "pattern match" on the result in a way that is
   strongly typed. If you pass exceptions and failures as data, then you can
   "generalize and cross boundaries, decoupling your code from a specific
   service or technology or platform".

I felt that both of these points were a pretty big case for functional programming in general, but even if you hate functional programming, they are interesting concepts that can help expand your programming patterns toolbelt.

### DevOps for Desktop Apps

**By:** Ricardo Minguez Pablos

> Client applications have unique requirements for DevOps, this session will show you how to use Azure to deploy MSIX based applications in an efficient and secure way. We will cover branching strategies, versioning, packaging and automatic deployment using Azure Pipelines. Also we will discuss new features and deployment options enabled to desktop developers with .NET Core 3.

I tuned this talk out as soon as I realized that it was only for Windows 10 apps. Although, it does appear that it's much easier to deploy apps to Windows now, as long as you're only targeting Windows 10.

I did learn that you can store secure files in Azure DevOps that can be dropped into build pipelines, so that's pretty cool. The use case he presented was a release pipeline with automatic application signing.

For the rest of the talk, I started this document, and stared at my bash terminal while it ran a really important program of my own design:

```bash
while true; do echo "Butts"; done
```

### Microservices 101 - Getting Started with .NET Core and Kubernetes

**By:** Brady Gaster & Glenn Condron

**GitHub:** [Acquired by Microsoft]

> The description for this one is not important because I don't care enough to look it up. Also, I couldn't find the description by searching Microsoft.com, therefore it apparently it doesn't matter, because the only things you need in your dev workflow are services owned by Microsoft.

This talk barely covered .NET Core. It also barely covered Kubernetes. This talk very much covered:

- The architectural design of a fictional online "Rock, Paper, Scissors" game
  made up of multiple web services and web service workers.
- Razor Pages
- gRPC (and the fact that one of the speakers fixed a bug with gRPC)
- What's going on at Microsoft
- All of the Microsoft services that you need to provision in order to get their
  sample app working.
  - Azure Config Service
  - Azure Messaging Queues
  - Azure Cosmos DB
  - gRPC (I guess)
- How to configure a .NET (Core?) app to talk to all of the services except
  Kubernetes, which is managed separately.

It was pretty fast paced, so I wasn't able to take coherent notes on anything useful. Also, it didn't really cover the topics presented in the description and title. The rest of it was spent loosely advertising Microsoft products. "101" should imply that we're going to leverage the power of Kubernetes and .NET Core for something trivial, not the power-lifting, use-case that Kubes was designed for running at enterprise scale. This wasn't a 101, this was a 301. I take that back actually, as long as you make it $101.

I'm still a little upset about this one.

### Improve Your Testing with Visual Studio 2019

**By:** Kendra Havens

**GitHub:** https://github.com/kendrahavens

> We’ve made several improvements to the test experience in Visual Studio to help developers write tests effectively. Come learn about the new test explorer features including better sorting, filtering, and a customizable hierarchy view! This talk will also cover some main principles of testing we think about when developing testing tools. You’ll also see demos on test generation with IntelliTest, code coverage tools, and the latest in Live Unit Testing. This talk will be demo-packed with lots of productivity tips and tricks along the way.

This talk showed off new features of the Visual Studio test explorer, with some demonstrations showing the remarkable performance improvements of discovering and running tests within Visual Studio. The IntelliTest features look interesting, but they seem to mostly cover null reference exceptions, divide by 0 errors, and other obvious gotchas. The biggest takeaway is that there appears to have been some TLC given exclusively to the Test Explorer in this iteration, and it shows.

## Talks Attended - Day 3

### Modern .NET Desktop Development in .NET Core 3

**By:** Olia Gavrysh

**GitHub:** https://github.com/OliaG

> .NET Core 3 is coming and with it support for building WinForms and WPF applications for Windows Desktop. Get an in-depth look at porting desktop applications to .NET Core 3 including implications for tooling and custom controls, along with how to leverage the best of .NET Core from your desktop applications.

I'm still confused by the topic but it's cool that .NET Core 3 is adding Winforms and WPF. I still think it's weird that .NET Core 3 is getting features that only work on Windows, but I don't work at Microsoft so what do I know?

This was another talk where Microsoft-specific services managed to find a way to creep in. Olia demonstrated a written-text transcription service that was pretty neat, but otherwise not useful to anything I'm working on.

I was initially confused as to the direction of the talk, so I looked up Olia part way though her presentation and realized that she was another one of the Project Managers that Microsoft sent to DEVintersection. That cleared things right up.

### The 8 most common ways developers get UX wrong

**By:** Billy Hollis

> Most developers have zero training in creating effective user experiences, so it's not surprising that they make mistakes. In this session, Billy Hollis will go through the most common UX mistakes he’s seen in business applications. Some of them include crowded screens, layout that’s too static, poor use of color, and failure to visualize data. In each case, there will be an example of the problem, with one or more alternatives that move towards fixing the problem. This will be an interactive session, with attendees encouraged to rate the alternatives and suggest their own ideas, and with a healthy question and answer session at the end.

Easily the most productive session that I went to. Most of his gripes felt like they were directed right at the products that most of the people in the room work on every single day. No feelings were spared.

The session was very well presented and interactive. I enjoyed this presentation the most out of the whole conference. I made sure to take as thorough notes as I could.

## Biggest Takeaways from DEVintersection Spring 2019

Of all the talks that I attended this year, I found 3 to be both interesting, and immediately useful. In no particular order:

- The 8 most common ways developers get UX wrong
- Zero to Database with EF Core Code First in 60 minutes
- Functional Techniques for C#

In these talks, I managed to get a better frame of mind as to how to think about UI in terms of UX. I may not have any of the required talent or practice or experience, but I certainly have a new-found appreciation for my UX designer friends. I also worked through setting up a a demo application using EF Core, although the demonstration used code that is already available in Microsoft's official documentation. I also was able to expand my Functional Programming vocabulary, which I love to do.

Other than those tangible gains, I now feel more comfortable messaging a Microsoft PM directly. Before DEVintersection, I would have had to lead with "Hey! I have a question about a project that you manage." Now I can say "Hey! I saw you at DEVintersection! I have a question about a project that you manage."

As for the rest of the conference, I have only neutral and negative opinions. A couple of the other things that made this conference annoying:

- Most of the sessions I attended were just not up to par with what I was
  expecting. My expectations were neutral, but the talks were still below what I
  believed we were paying for.
- I remember enjoying the panels but I don't remember any takeaways.
- I participated in every raffle but didn't win anything except for a new wave
  of email notifications.
- It was all the way down in Orlando at Disney, so I had to pay Disney prices
  for everything but didn't have enough time to enjoy the park.

The coolest thing about the conference was getting to experience Scott Hanselman for the first time. He demoed .NET Core on a RaspberryPI. Apparently they're adding a `System.Devices.Gpio` namespace, which is just absolute insanity. Way to go guys. I don't know how I'll use it, but I suppose that it's rad.

I guess that's kind of how I felt at DEVintersection in general.

## Conclusion

Last year at RevConf, I had the opportunity to dive headfirst into Docker, which changed my whole view of backend programming and infrastructure.

This year at DEVintersection, I worked through some sample code for EF Core and Functional C#, which was useful but not mind-blowing.

I think that about sums it up.

It cost my company over $3200 to send me to Florida for this conference for a week. That's a rough estimate that will certainly go up once I start filling out expense reports. That figure also fails to consider the lost productivity, which is always inconvenient for everyone involved.

For all of the issues that I had with RevConf last year, I think I would have enjoyed going to that this year instead. DEVintersection was at a much flashier location and was a distinctly larger event, but I don't see how the extra cost was justified. It certainly didn't translate to bigger takeaways. I just don't see how DEVintersection was $2800 BETTER than RevConf.

If you're thinking of going to DEVintersection, but there's also a much-cheaper conference that's happening around the same time, closer to home, then I'd recommend option 2. It may also be a reflection of my biases, but I feel that investing time and money into your local development communities is more important than struggling to make connections at an international conference, where you likely will not see any of the attendees ever again.

I'd go again, but not with my own money.
