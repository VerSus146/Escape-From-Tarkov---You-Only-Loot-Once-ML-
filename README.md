# **Escape From Tarkov - You Only Loot Once - Machine Learning**

## **Problem**
_Why? For whom?_

This project aims to provide _begginers_ with additional information about their equipment.
EFT YOLO will use Transferred Learning to detect objects in character equipment tab.
The tool won't be using any of the game's code. All testing has been performed in offline mode - use of it in online play can result in account bans.

## **Technicals**
_How?_

EFT YOLO will leverage YOLOv8 functionality to provide fast and lightweight resolution to many problems of beginner user players.
The main problem with Tarkov's equipment are slight small changes to all of the object visible in the EQ being projections of 3D Objects to 2D Plane.
Additionally, the equippment has slight transparency that changes the background of all items in-raid, especially during various times of the day.

The dataset will consist of a mix of synthetic and real screenshots labeled via LabelMe which will be translated to YOLO format by labelme2yolo library.
Technically, if we are creating synthetic screenshots (modified) the LabelMe labels from the originals should be reusable on the copies, hugely improving the 
labeling effort.

After detection, the program will use existing [Trading APIs](https://tarkov-market.com/dev/api) to check item prices of player's loot.

As a POC, the model will be detecting medical equipmnet. After detection, an easy to use tool will be created to better present the data to the end-user.
The presentation tool will have a set of filter and ways to display prices, like Gradient from Red to Purple (Red > Yellow > Green > Blue > Purple) showing how valuable the item is
or simply display the prices of given items after hovering over the item using mouse.

All of the training will be performed on my laptop with RTX 4060 - hopefully it will survive it. :)

## **Who am I?**
At the time of me creating this document I am a Manual QA Lead at Intel Corporation. I am responsible for various projects which mostly focus on driver testing
using benchmarks, games and WSTN tools. After 6 years in testing field I feel like it's a great moment to start learning something new. :)
I have recently finished [Zero to Mastery PyTorch Training](https://www.learnpytorch.io) and I think I am ready for my first small ML project.
Transferred Learning is very easy to use, hence why these are my first steps. Small updates will be delivered here and there, but I am very excited to work on this project.
Hopefully it will ultimatelly see the light of day! <3 
