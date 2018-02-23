# eigenface
Use PCA to create eigenfaces. 

# F A Q
### What is PCA?
Principle Component Analysis (PCA) is a statistical method that transforms an n-dimensional data set (via orthogonal matrix multiplication) into its "closest" k-dimensional approximation. 

### What is an Eigenface?
Within the context of image classification (here, specifically face recognition), the data is a set of images. The **features** (i.e., the dimensions) of this dataset are the images themselves, each represented by a vector $f_i$ of pixel intensities.

<img src="https://github.com/elisabeth-berg/eigenface/blob/master/img/matrix.png" width="350" height="200">

Then, given a sufficiently large set of face vectors <a href="http://www.codecogs.com/eqnedit.php?latex={f_1,&space;f_2,&space;...&space;f_p}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?{f_1,&space;f_2,&space;...&space;f_p}" title="{f_1, f_2, ... f_p}" /></a>, 
any face can be approximately reconstructed as a linear combination of these <a href="http://www.codecogs.com/eqnedit.php?latex=f_i" target="_blank"><img src="http://latex.codecogs.com/gif.latex?f_i" title="f_i" /></a>s. For example, 

<a href="http://www.codecogs.com/eqnedit.php?latex=f_{matt}&space;\approx&space;0.2&space;f_{brett}&space;&plus;&space;0.4&space;f_{miller}&space;&plus;&space;...&space;&plus;&space;0.02&space;f_{christie}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?f_{matt}&space;\approx&space;0.2&space;f_{brett}&space;&plus;&space;0.4&space;f_{miller}&space;&plus;&space;...&space;&plus;&space;0.02&space;f_{christie}" title="f_{matt} \approx 0.2 f_{brett} + 0.4 f_{miller} + ... + 0.02 f_{christie}" /></a>.

Of course, the more face vectors used, the better the approximation. 

Now, PCA can be applied to the feature matrix X, transforming each face vector into an **eigenface** vector. There are still p of these vectors, each eigenface vector still contains pixel intensity values, and a facial image can still be reconstructed as a linear combination of the eigenfaces. However, an eigenface does not correspond to a specific face from the original data set. Instead, it is an amalgamation of all the faces, now representing the presence and prevalence of a given image feature. 

The advantage to using eigenface vectors (rather than the original face vectors) to approximate facial images is that the set of eigenface vecors is **linearly independent**. This means that if we drop an eigenface vector from the set, we lose the information contained in just that single vector (this is not the case with the original face vectors, in which dropping a single vector results in reduced information for *many* features).  Thus, we can easily reduce the dimensionality of the set of faces by retaining only the k most important eigenfaces. This transforms a data set of dimension p into a set of dimension k. 
