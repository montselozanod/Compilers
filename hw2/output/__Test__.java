import java.io.*;
import org.antlr.runtime.*;
import org.antlr.runtime.debug.DebugEventSocketProxy;


public class __Test__ {

    public static void main(String args[]) throws Exception {
        patitoLexer lex = new patitoLexer(new ANTLRFileStream("/Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/output/__Test___input.txt", "UTF8"));
        CommonTokenStream tokens = new CommonTokenStream(lex);

        patitoParser g = new patitoParser(tokens, 49100, null);
        try {
            g.parse();
        } catch (RecognitionException e) {
            e.printStackTrace();
        }
    }
}