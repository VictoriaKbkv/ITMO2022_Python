import java.io.*;
import java.math.BigDecimal;
import java.util.Random;

public class DGEMM {

    public int[][] retrievedMatrixInt(int m, int n, File file) {
        int [][] matrix = new int[m][n];
        try (BufferedReader reader = new BufferedReader(new FileReader(file))) {
            String line;
            int lineCount = 0;
            while ((line = reader.readLine()) != null){
                int columnCount = 0;
                String [] values = line.split(" ");
                for (String value : values) {
                    matrix[lineCount][columnCount] = Integer.parseInt(value);
                    columnCount++;
                }
                lineCount++;
            }
        } catch (IOException e) {
            System.out.println(e.getMessage());
        }
        return matrix;
    }

    public double[][] retrievedMatrixDouble(int m, int n, File file) {
        double [][] matrix = new double[m][n];
        try (BufferedReader reader = new BufferedReader(new FileReader(file))) {
            String line;
            int lineCount = 0;
            while ((line = reader.readLine()) != null){
                int columnCount = 0;
                String [] values = line.split(" ");
                for (String value : values) {
                    matrix[lineCount][columnCount] = Double.parseDouble(value);
                    columnCount++;
                }
                lineCount++;
            }
        } catch (IOException e) {
            System.out.println(e.getMessage());
        }
        return matrix;

    }

    public BigDecimal[][] retrievedMatrixBigDecimal(int m, int n, File file) {
        BigDecimal[][] matrix = new BigDecimal[m][n];
        try (BufferedReader reader = new BufferedReader(new FileReader(file))) {
            String line;
            int lineCount = 0;
            while ((line = reader.readLine()) != null){
                int columnCount = 0;
                String [] values = line.split(" ");
                for (String value : values) {
                    BigDecimal bigDecimal = new BigDecimal(value);
                    matrix[lineCount][columnCount] = bigDecimal;
                    columnCount++;
                }
                lineCount++;
            }
        } catch (IOException e) {
            System.out.println(e.getMessage());
        }
        return matrix;

    }

    public double[] getCoef(File file, int numberOfCoef) {
        double [] coef = new double[numberOfCoef];
        try (BufferedReader reader = new BufferedReader(new FileReader(file))) {
            String line;
            int lineCount = 0;
            while ((line = reader.readLine()) != null){
                coef[lineCount] = Double.parseDouble(line);
                lineCount++;
            }
        } catch (IOException e) {
            System.out.println(e.getMessage());
        }
        return coef;
    }

    public void Calculate(int startRow, int finishRow, double[][] matrixA, double[][] matrixB, double[][] matrixC, double[][] newC, double alpha, double beta) {
        for (int i = startRow; i < finishRow; i++) {
            for (int j = 0; j < matrixC[0].length; j++) {
                for (int r = 0; r < matrixA[startRow].length; r++) {
                    newC[i][j] = newC[i][j] + alpha * matrixA[i][r]*matrixB[r][j];
                }
                newC[i][j] = newC[i][j] + beta * matrixC[i][j];
            }
        }
    }

    public void Calculate(int startRow, int finishRow, int[][] matrixA, int[][] matrixB, int[][] matrixC, int[][] newC, int alpha, int beta) {
        for (int i = startRow; i < finishRow; i++) {
            for (int j = 0; j < matrixC[0].length; j++) {
                for (int r = 0; r < matrixA[startRow].length; r++) {
                    newC[i][j] = newC[i][j] + alpha * matrixA[i][r]*matrixB[r][j];
                }
                newC[i][j] = newC[i][j] + matrixC[i][j];
            }
        }
    }

    public void Calculate(int startRow, int finishRow, BigDecimal[][] matrixA, BigDecimal[][] matrixB, BigDecimal[][] matrixC, BigDecimal[][] newC, BigDecimal alpha, BigDecimal beta) {
        for (int i = startRow; i < finishRow; i++) {
            for (int j = 0; j < matrixC[0].length; j++) {
                for (int r = 0; r < matrixA[startRow].length; r++) {
                    newC[i][j] = newC[i][j].add((matrixA[i][r].multiply(matrixB[r][j])).multiply(alpha));
                }
                newC[i][j] = newC[i][j].add(matrixC[i][j]);
            }
        }
    }

    public void writeMatrixToFile(double[][] matrix, File file){
        try (PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter(file, false)))) {
            for (int i = 0; i < matrix.length; i++) {
                for (int j = 0; j < matrix[0].length; j++) {
                    out.print(matrix[i][j]);
                    out.print(' ');
                }
                out.print('\n');
            }
        } catch (IOException e) {
            System.out.println(e.getMessage());
        }
    }

    public void writeMatrixToFile(int[][] matrix, File file){
        try (PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter(file, false)))) {
            for (int i = 0; i < matrix.length; i++) {
                for (int j = 0; j < matrix[0].length; j++) {
                    out.print(matrix[i][j]);
                    out.print(' ');
                }
                out.print('\n');
            }
        } catch (IOException e) {
            System.out.println(e.getMessage());
        }
    }

    public void writeMatrixToFile(BigDecimal[][] matrix, File file){
        try (PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter(file, false)))) {
            for (int i = 0; i < matrix.length; i++) {
                for (int j = 0; j < matrix[0].length; j++) {
                    out.print(matrix[i][j]);
                    out.print(' ');
                }
                out.print('\n');
            }
        } catch (IOException e) {
            System.out.println(e.getMessage());
        }
    }
}
