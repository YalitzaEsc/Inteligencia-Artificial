import java.util.*;

public class SearchTree {
    private Node root;
    private String goalSate;

    public Node getRoot() {
        return root;
    }

    public void setRoot(Node root) {
        this.root = root;
    }

    public String getGoalSate() {
        return goalSate;
    }

    public void setGoalSate(String goalSate) {
        this.goalSate = goalSate;
    }

    public SearchTree(Node root, String goalSate) {
        this.root = root;
        this.goalSate = goalSate;
    }

    // Búsqueda en anchura
    public void breadthFirstSearch() {
        Set<String> stateSets = new HashSet<>();
        Node node = new Node(root.getState());
        Queue<Node> queue = new LinkedList<>();
        Node currentNode = node;
        while (!currentNode.getState().equals(goalSate)) {
            stateSets.add(currentNode.getState());
            List<String> nodeSuccessors = NodeUtil.getSuccessors(currentNode.getState());
            for (String n : nodeSuccessors) {
                if (stateSets.contains(n))
                    continue;
                stateSets.add(n);
                Node child = new Node(n);
                currentNode.addChild(child);
                child.setParent(currentNode);
                queue.add(child);
            }
            currentNode = queue.poll();
        }
        NodeUtil.printSolution(currentNode, stateSets, root);
    }

    // Búsqueda en profundidad
    public void depthFirstSearch() {
        Set<String> stateSets = new HashSet<>();
        Node node = new Node(root.getState());
        MyStack<Node> stack = new MyStack<>();
        Node currentNode = node;
        while (!currentNode.getState().equals(goalSate)) {
            stateSets.add(currentNode.getState());
            List<String> nodeSuccessors = NodeUtil.getSuccessors(currentNode.getState());
            for (String n : nodeSuccessors) {
                if (stateSets.contains(n))
                    continue;
                stateSets.add(n);
                Node child = new Node(n);
                currentNode.addChild(child);
                child.setParent(currentNode);
                stack.push(child);
            }
            currentNode = stack.pop();
        }
        NodeUtil.printSolution(currentNode, stateSets, root);
    }
}
