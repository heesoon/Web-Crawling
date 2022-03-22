package com.apress.prospring5.ch2.decoupled;

public class StandardOutMessageRenderer implements MessageRenderer {

    private MessageProvider messageProvider;

    public StandardOutMessageRenderer(){
        System.out.println(" --> StandardOutMessageRenderer() called");
    }

    @Override
    public void render() {
        if (messageProvider == null) {
            throw new RuntimeException(
                    StandardOutMessageRenderer.class.getName() 
                    + " messageProvider class properties setted");
        }
        System.out.println(messageProvider.getMessage());
    }

    @Override
    public void setMessageProvider(MessageProvider provider) {
        System.out.println(" --> StandardOutMessageRenderer: messageProvider setting");
        this.messageProvider = provider;
    }

    @Override
    public MessageProvider getMessageProvider() {
        return this.messageProvider;
    }
}
