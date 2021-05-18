Extract both the files in a folder. The provided jar can compute the readability of a snippet and the readability of a class (mean readability of its methods). The output depends on the provided input file.

To run the jar, use the following command, specifying at least a file name:
java -jar rsm.jar {filename} [{filename2} {filename3} ... {filenameN}]

Example:
java -jar rsm.jar test.java

You can also run it on many files. 
Examples:
java -jar rsm.jar test.java test2.java
java -jar rsm.jar src/**/*.java

You can export the values of all the metrics by using the following command:
java -cp rsm.jar it.unimol.readability.metric.runnable.ExtractMetrics {filename}

Example:
java -cp rsm.jar it.unimol.readability.metric.runnable.ExtractMetrics test.java
