import java.io.File;

public class Main {
    public static void main(String[] args) {

        int min = 10;
        int max = 99;

        int numberOfCoef = 5;

        double [] coef;
        File fileCoef = new File("C:\\Users\\Victoria\\Documents\\ITMO_Course\\Python\\ITMO2022_Python\\Files_Practice2\\Coef.txt");
        coef = MatrixGenerator.getCoef(fileCoef, numberOfCoef);
        int M = (int)coef[0];
        int N = (int)coef[1];
        int K = (int)coef[2];

        File fileA = new File("C:\\Users\\Victoria\\Documents\\ITMO_Course\\Python\\ITMO2022_Python\\Files_Practice2\\MatrixA.txt");
        MatrixGenerator.generateDouble(min, max, M, N, fileA);

        File fileB = new File("C:\\Users\\Victoria\\Documents\\ITMO_Course\\Python\\ITMO2022_Python\\Files_Practice2\\MatrixB.txt");
        MatrixGenerator.generateDouble(min, max, N, K, fileB);

        File fileC = new File("C:\\Users\\Victoria\\Documents\\ITMO_Course\\Python\\ITMO2022_Python\\Files_Practice2\\MatrixC.txt");
        MatrixGenerator.generateDouble(min, max, M, K, fileC);
    }
}
