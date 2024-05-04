<style type="text/css">
			header, section, footer, aside, nav, article, figure, figcaption {
				display: block;}
			body {
				color: #666666;
				background-color: #f9f8f6;
				background-image: url("imgs/background.jpg");
				background-position: center;
				font-family: Georgia, Times, serif;
				line-height: 1.4em;
				margin: 0px;}
			.wrapper {
				width: 940px;
				margin: 20px auto 20px auto;
				border: 1px solid #555555;
				background-color: #ffffff;}
			header {
				height: 160px;
				background-image: url("images/header.jpg");}
			h1 {
				text-indent: -9999px;
				width: 940px;
				height: 130px;
				margin: 0px;}
			nav, footer {
				clear: both;
				color: #ffffff;
				background-color: #aeaca8;
				height: 30px;}
			nav ul {
				margin: 0px;
				padding: 5px 0px 5px 30px;}
			nav li {
				display: inline;
				margin-right: 40px;}
			nav li a {
				color: #ffffff;}
			nav li a:hover, nav li a.current {
				color: #000000;}
			section.leftWindow {
				float: left;
				width: 659px;
				border-right: 1px solid #eeeeee;}
			article {
				clear: both;
				overflow: auto;
				width: 100%;}
			hgroup {
				margin-top: 40px;}
			figure {
				float: left;
				width: 290px;
				height: 220px;
				padding: 5px;
				margin: 20px;
				border: 1px solid #eeeeee;}
			figcaption {
				font-size: 90%;
				text-align: left;}
			aside {
				width: 230px;
				float: left;
				padding: 0px 0px 0px 20px;}
			aside section a {
				display: block;
				padding: 10px;
				border-bottom: 1px solid #eeeeee;}
			aside section a:hover {
				color: #985d6a;
				background-color: #efefef;}
			a {
				color: #de6581;
				text-decoration: none;}
			h1, h2, h3 {
				font-weight: normal;}
			h2 {
				margin: 10px 0px 5px 0px;
				padding: 0px;}
			h3 {
				margin: 0px 0px 10px 0px;
				color: #de6581;}
			aside h2 {
				padding: 30px 0px 10px 0px;
				color: #de6581;}
			footer {
				font-size: 80%;
				padding: 7px 0px 0px 20px;}
		</style>
<div class="wrapper">
  <nav>
  <ul>
	<li><a href="https://rmec.gitee.io" class="current">Home</a></li>
	<li><a href="https://mooc1.chaoxing.com/course/214592125.html ">超星慕课</a><li>  
  </ul>
  </nav>


## 数据建模与分析(3XS091017)-2020年秋季

* 教师: 姚远 
* Email: yaoyuan@shu.edu.cn
* 时间: 周二5-8节 13:00 - 16:45
* 地点: HB2204
* 学校e-learning主页: https://mooc1.chaoxing.com/course/219557466.html  



## 课程目标

数据处理与分析是当今现代科学技术研究的主要手段，其技术己渗透到各学科和工程技术领域。本课程以一般系统理论为基础，介绍了建模与仿真的一般理论框架、思想和方法。帮助一年级研究生理解数据分析、结构建模、可视化建模、人工神经网络建模的概念，能够通过比较分析、量纲分析、结构分析、统计分析和面向对象分析等方法建立模型，并掌握通过模型进行仿真分析的实用方法。 

## 课程作业
本课程的作业可从课程所留作业中任选一个，要求撰写报告，并与相关代码一起提交到超星慕课。
学硕课程提交地址：超星慕课->[数据建模与分析](https://mooc1.chaoxing.com/course/214592125.html)->课程作业
专硕课程提交地址：超星慕课->[建模与仿真]( https://mooc1.chaoxing.com/course/214592131.html )->课程作业
如无加入，请先加入班级。

**邮件递交**
  - Email Title:" 学号-姓名-课程名称-报告标题"，例如 20925776-吴兴名-数据建模与分析-统计学习作业报告
  - 地址：Frewing@qq.com
  - 
报告模板 [word](homework/homeworkTpl.docx)






## 课程安排

1. 工业互联网趋势与关键问题 (09-17)

2. 建模与仿真基础(09-24)

   [lecture-1](lectures/lecture1-IntroductionModeling-Simulation.pdf)

3. 十一停课(10-01)

4. 数据与数据处理(10-10)

   [lecture-2](lectures/lecture-2-Data.pdf)

   - 作业1数据
     ```
     #生成数据(使用python sklearn包中的make_moons数据集)
     from sklearn.datasets import make_moons
     X, y = make_moons(200, noise=.05, random_state=0)     
     ```
     [data.csv](homework/mdata4clustering.csv)

5. 数字几何建模与3D打印模型处理(10-15)

   [lecture-3](lectures/lecture3-Geometry.pdf)
   - 作业2参考代码框架
     [c++ code](https://gitee.com/combust/info/raw/master/suSlicer.rar)

6. 数据建模-统计学习基础(10-22)
   [lecture-4](lectures/lecture4-StatisticalLearning.pdf)
   - 作业3参考代码框架
     [python code](https://gitee.com/combust/info/raw/master/pythonLG.rar)
     [matlab code](https://gitee.com/combust/info/raw/master/matlabLG.rar)

7. 神经网络(10-29)

   [lecture-5](lectures/lecture5-ANN.pdf)

8. 系统估计与人工系统建模(11-05) 
   [lecture-6-1](lectures/lecture6-KalmanFilter.pdf)
   [lecture-6-2](lectures/lecture6-ExpertSystem.pdf)

9. 课堂报告(11-12) 
   - 


10. 课堂考试 (11-19) 

</div>