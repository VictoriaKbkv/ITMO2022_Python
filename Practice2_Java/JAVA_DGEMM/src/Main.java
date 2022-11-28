import java.io.File;

public class Main {

    public static void main(String[] args) {
        final int numberOfCoef = 5;
        File fileA = new File("C:\\Users\\Victoria\\Documents\\ITMO_Course\\Python\\ITMO2022_Python\\Files_Practice2\\MatrixA.txt");
        File fileB = new File("C:\\Users\\Victoria\\Documents\\ITMO_Course\\Python\\ITMO2022_Python\\Files_Practice2\\MatrixB.txt");
        File fileC = new File("C:\\Users\\Victoria\\Documents\\ITMO_Course\\Python\\ITMO2022_Python\\Files_Practice2\\MatrixC.txt");
        File fileCoef = new File("C:\\Users\\Victoria\\Documents\\ITMO_Course\\Python\\ITMO2022_Python\\Files_Practice2\\Coef.txt");
        File fileNewC = new File("C:\\Users\\Victoria\\Documents\\ITMO_Course\\Python\\ITMO2022_Python\\Files_Practice2\\MatrixC_new.txt");
        double [] coef;
        double [][] matrixA;
        double [][] matrixB;
        double [][] matrixC;
        int M;
        int N;
        int K;
        double alpha;
        double beta;

        DGEMM dgemm = new DGEMM();
        coef = dgemm.getCoef(fileCoef, numberOfCoef);
        M = (int)coef[0];
        N = (int)coef[1];
        K = (int)coef[2];
        alpha = coef[3];
        beta = coef[4];
        double [][] matrixNewC = new double[M][K];
        matrixA = dgemm.retrievedMatrixDouble(M, N, fileA);
        matrixB = dgemm.retrievedMatrixDouble(N, K, fileB);
        matrixC = dgemm.retrievedMatrixDouble(M, K, fileC);
        dgemm.Calculate(0, M, matrixA, matrixB, matrixC, matrixNewC, alpha, beta);
        dgemm.writeMatrixToFile(matrixNewC, fileNewC);
    }
}
