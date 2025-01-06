import React, {useState, useEffect, useRef} from 'react';
import './App.css';

import axios, { mergeConfig } from 'axios';

interface Message {
    text: string;
    sender: 'user' | 'bot'
}


function App () {
    const [messages, setMessages] = useState<Message[]>([])
    const [userInput, setUserInput]  = useState('');
    const [isBotTyping, setIsBotTyping] = useState(false);
    const messagesEndRef = useRef<HTMLDivElement>(null);

    useEffect(() => {
        if(messagesEndRef.current){
            messagesEndRef.current.scrollIntoView({behaviour: 'smooth'});
        }
    }, [messagesEndRef]);

    const sendMessage  = async () => {
        if(userInput.trim === '') return;
        setMessages([...messages, {text: userInput, sender: 'user'}]);
        setUserInput('');
        setIsBotTyping(true);
        
        try {
            const response = await axios.post('http://localhost:5000/api/chat', {message: userInput});
            setMessages(prev => [... prev, {text: response.data.response, sender: 'bot'}])
        } catch (error){
            console.error('Error sending message', error);
            setMessages(prev => [...prev, {text: 'Error communicating with server', sender: 'bot'}])
        }  finally {
            setIsBotTyping(false);
        }
    }

    return (
        <div className='chat-container'>
            <div className='message-list'>
                {messages.map((msg, i) => (
                    <div key={i} className={`message ${msg.sender}`}>
                        {msg.text}
                    </div>
                ))}
                <div ref={messagesEndRef} />
            </div>
            {isBotTyping && (
              <div className='message bot'>
                <div className='typing-indicator'>
                  <span>.</span><span>.</span><span>.</span>
                </div>
              </div>
            )}
            <div className='input-area'>
                <input
                    type='text'
                    value={userInput}
                    onChange={e => setUserInput(e.target.value)}
                    onKeyDown={e => e.key === 'enter' && sendMessage()}
                />
                <button onClick={sendMessage}>send</button>
            </div>
        </div>
    );

}

export default App;
