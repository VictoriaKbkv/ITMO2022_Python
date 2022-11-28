import java.io.File;
import java.math.BigDecimal;
import java.util.Arrays;

public class BigDecimalMain {
    public static void main(String[] args) {
        final int numberOfCoef = 5;
        File fileA = new File("C:\\Users\\Victoria\\Documents\\ITMO_Course\\Python\\ITMO2022_Python\\Files_Practice2\\MatrixA.txt");
        File fileB = new File("C:\\Users\\Victoria\\Documents\\ITMO_Course\\Python\\ITMO2022_Python\\Files_Practice2\\MatrixB.txt");
        File fileC = new File("C:\\Users\\Victoria\\Documents\\ITMO_Course\\Python\\ITMO2022_Python\\Files_Practice2\\MatrixC.txt");
        File fileCoef = new File("C:\\Users\\Victoria\\Documents\\ITMO_Course\\Python\\ITMO2022_Python\\Files_Practice2\\Coef.txt");
        File fileNewC = new File("C:\\Users\\Victoria\\Documents\\ITMO_Course\\Python\\ITMO2022_Python\\Files_Practice2\\MatrixC_new.txt");
        double [] coef;
        BigDecimal[][] matrixA;
        BigDecimal [][] matrixB;
        BigDecimal [][] matrixC;
        int M;
        int N;
        int K;

        DGEMM dgemm = new DGEMM();
        coef = dgemm.getCoef(fileCoef, numberOfCoef);
        M = (int)coef[0];
        N = (int)coef[1];
        K = (int)coef[2];
        BigDecimal alpha = new BigDecimal(coef[3]);
        BigDecimal beta = new BigDecimal(coef[4]);
        BigDecimal [][] matrixNewC = new BigDecimal[M][K];
        for (BigDecimal[] row : matrixNewC) {
            Arrays.fill(row, BigDecimal.ZERO);
        }
        matrixA = dgemm.retrievedMatrixBigDecimal(M, N, fileA);
        matrixB = dgemm.retrievedMatrixBigDecimal(N, K, fileB);
        matrixC = dgemm.retrievedMatrixBigDecimal(M, K, fileC);
        dgemm.Calculate(0, M, matrixA, matrixB, matrixC, matrixNewC, alpha, beta);
        dgemm.writeMatrixToFile(matrixNewC, fileNewC);
    }
}
