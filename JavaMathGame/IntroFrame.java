import java.awt.*;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;

import javax.swing.*; // This is for graphics.

public class IntroFrame implements MouseListener{
	private JFrame frame;
    private drawingPanel panel;
    private final int W = 800;
    private final int HT = 800;
    
    public IntroFrame(){
    	frame = new JFrame("Intro");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        panel = new drawingPanel();
        panel.setPreferredSize(new Dimension(W, HT));
        frame.getContentPane().add(panel);
        frame.pack(); // Get the frame all ready.
        panel.addMouseListener(this);
    }
    
    public void visible(boolean b){
    	frame.setVisible(b);
    }
    
    private class drawingPanel extends JPanel{
        public void paintComponent(Graphics g){
            super.paintComponent(g);
            g.setFont(new Font("Arial", 0, 100));
            g.drawString("Practice Your", 100, 100);
            g.drawString("Math Skills!", 150, 200);
			// Draw the start button.
            g.setColor(Color.getHSBColor(.4f, .8f, .8f));
            g.fillRect(200, 500, 400, 200);
            g.setColor(Color.getHSBColor(.65f, 1f, .5f));
            g.drawString("GO!", 310, 630);
        }
    }

	@Override
	public void mouseClicked(MouseEvent arg0) {
		// This says "if they click where the start button is, then start the game."
		if (arg0.getX() > 200 && arg0.getX() < 600 && arg0.getY() > 400 && arg0.getY() < 600){
			visible(false);
			Main.gf.visible(true);
		}
	}

	@Override
	public void mouseEntered(MouseEvent e) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public void mouseExited(MouseEvent e) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public void mousePressed(MouseEvent e) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public void mouseReleased(MouseEvent e) {
		// TODO Auto-generated method stub
		
	}
}

