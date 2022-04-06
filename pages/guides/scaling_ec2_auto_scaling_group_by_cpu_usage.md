# Scaling EC2 Auto Scaling Group by CPU Usage

Follow these instructions to setup Auto Scaling based on CPU Usage average across the EC2 Instances in the Auto Scaling Group over a defined period of time (By default this is 5 minutes).

* Open up the AWS Console and browse to EC2 > Auto Scaling Groups (On the left hand side)
* Select the Auto Scaling Group that You wish to apply the scaling to and select “Scaling Policies“ from the menu at the bottom.
* Create two new Policies as follows:
  * Click the Link to create a Scaling Policy with Steps
  * Name: Scale Down CPU
    * Execute policy when: (Create new alarm)
        * Send Notification to: your@domain.com
        * When average of “CPU Utilization” is <= 70% for 1 period of 5 minutes.
        * Name of Alarm: awsec2-[Autoscaling Group]-Low-CPU-Utilization
    * Take the Action: Remove 1 capacity units when 70% >= CPUUtilization
  * Name: Scale Up CPU
    * Execute policy when: (Create new alarm)
        * Send Notification to: your@domain.com
        * When average of “CPU Utilization” is >= 70% for 1 period of 5 minutes.
        * Name of Alarm: awsec2-[Autoscaling Group]-High-CPU-Utilization
    * Take the Action: Add 1 capacity units when 70% <= CPUUtilization
    * Instances need: 720 seconds to warm up