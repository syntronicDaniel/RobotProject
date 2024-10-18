# How to deal with this shenanigans

## Set up your model
* Make a package for you model.
```sh
ros2 pkg create --build-type ament_cmake RobotModelPackageName
```
* Use .urdf model to make your robot model.
 - You can either create one or find one. It's good to make one, or atleast follow up on how one is made as it's quite simple.
 - Place your model in root_ws/src/RobotModelPackageName/urdf/RobotModelName.urdf
 - Write with your preffered text editor. 
 - Feel free to look at some examples. There are plenty of 4 wheeled robot models out there

