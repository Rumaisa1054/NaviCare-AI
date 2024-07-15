import streamlit as st
import base64
import responser as rn
# Function to convert image to base64
def get_image_as_base64(file_path):
    with open(file_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

image_base64 = get_image_as_base64("heartbeat.png")

# Define the actions
def find_a_doctor():
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown('<div style="margin-top: -25px; margin-left: -200px;" class="title-wrapper"><h1 style="text-align: center;">Find A Doctor</h1></div>', unsafe_allow_html=True)
        
    with col2:
        if st.button("_Back_",use_container_width=True):
            st.session_state.action = None
    
    # Initialize chat history for chat tab
    if "chat_messages" not in st.session_state:
        st.session_state.chat_messages = []
    
    # Display chat messages from history on a container
    for message in st.session_state.chat_messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # React to user input
    if prompt := st.chat_input("Welcome to NaviCare AI - How can I help You?"):
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)
        # Add user message to chat history
        st.session_state.chat_messages.append({"role": "user", "content": prompt})
    
        response = rn.doc_runner(prompt)
        # Display assistant response in chat message container
        with st.chat_message("NaviCare AI Bot"):
            st.markdown(response)
        # Add assistant response to chat history
        st.session_state.chat_messages.append({"role": "assistant", "content": response})
    

def appointment_maker():
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown('<div style="margin-top: -25px; margin-left: -200px;" class="title-wrapper"><h1 style="text-align: center;">Appointment Maker</h1></div>', unsafe_allow_html=True)
    with col2:
        if st.button("_Back_",use_container_width=True):
            st.session_state.action = None
    
    # Initialize chat history for chat tab
    if "apt_messages" not in st.session_state:
        st.session_state.apt_messages = []
    
    # Display chat messages from history on a container
    for message in st.session_state.apt_messages:
        with st.apt_messages(message["role"]):
            st.markdown(message["content"])
    
    # React to user input
    if prompt := st.chat_input("Welcome to NaviCare AI - How can I help You?"):
        # Display user message in chat message container
        with st.apt_messages("user"):
            st.markdown(prompt)
        # Add user message to chat history
        st.session_state.apt_messages.append({"role": "user", "content": prompt})
    
        response = "Here-------------------------------------------------2"
        # Display assistant response in chat message container
        with st.chat_message("NaviCare AI Bot"):
            st.markdown(response)
        # Add assistant response to chat history
        st.session_state.apt_messages.append({"role": "assistant", "content": response})
    

def visit_assistant():
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown('<div style="margin-top: -25px; margin-left: -200px;" class="title-wrapper"><h1 style="text-align: center;">Visit Assistant</h1></div>', unsafe_allow_html=True)
    with col2:
        if st.button("_Back_",use_container_width=True):
            st.session_state.action = None
    
    
    # Initialize chat history for chat tab
    if "visit_messages" not in st.session_state:
        st.session_state.visit_messages = []
    
    # Display chat messages from history on a container
    for message in st.session_state.visit_messages:
        with st.visit_messages(message["role"]):
            st.markdown(message["content"])
    
    # React to user input
    if prompt := st.chat_input("Welcome to NaviCare AI - How can I help You?"):
        # Display user message in chat message container
        with st.visit_messages("user"):
            st.markdown(prompt)
        # Add user message to chat history
        st.session_state.visit_messages.append({"role": "user", "content": prompt})
    
        response = "Here-------------------------------------------------3"
        # Display assistant response in chat message container
        with st.chat_message("NaviCare AI Bot"):
            st.markdown(response)
        # Add assistant response to chat history
        st.session_state.visit_messages.append({"role": "assistant", "content": response})
    

def wellness_advocate():
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown('<div style="margin-top: -25px; margin-left: -200px;" class="title-wrapper"><h1 style="text-align: center;">Wellness Adovocate</h1></div>', unsafe_allow_html=True)
    with col2:
        if st.button("_Back_",use_container_width=True):
            st.session_state.action = None
    
    # Initialize chat history for chat tab
    if "wellness_messages" not in st.session_state:
        st.session_state.wellness_messages = []
    
    # Display chat messages from history on a container
    for message in st.session_state.wellness_messages:
        with st.wellness_messages(message["role"]):
            st.markdown(message["content"])
    
    # React to user input
    if prompt := st.chat_input("Welcome to NaviCare AI - How can I help You?"):
        # Display user message in chat message container
        with st.wellness_messages("user"):
            st.markdown(prompt)
        # Add user message to chat history
        st.session_state.wellness_messages.append({"role": "user", "content": prompt})
    
        response = "Here-------------------------------------------------4"
        # Display assistant response in chat message container
        with st.chat_message("NaviCare AI Bot"):
            st.markdown(response)
        # Add assistant response to chat history
        st.session_state.wellness_messages.append({"role": "assistant", "content": response})
    

# Streamlit App
def main():
    if "action" not in st.session_state:
        st.session_state.action = None

    # Apply custom CSS to center the title and make buttons full-width
    st.markdown("""
        <style>
        /* Center the title */
        .title-wrapper {
            display: flex;
            justify-content: center;
            margin-bottom: 20px;  /* Optional: Adjust margin as needed */
        }
        /* Make buttons full-width */
        .full-width-button .stButton button {
            width: 100%;
            height: 50px;  /* Optional: Adjust the button height if needed */
        }
        </style>
    """, unsafe_allow_html=True)

    # Create placeholders for UI components
    title_placeholder = st.empty()
    image_placeholder = st.empty()
    buttons_placeholder = st.empty()

    if st.session_state.action is None:
        with title_placeholder.container():
            st.markdown('<div class="title-wrapper"><h1 style="text-align: center;">NaviCare AI</h1></div>', unsafe_allow_html=True)
        
        with image_placeholder.container():
            st.markdown("""
            <style>
            .container {
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                height: 4vh;
                margin: 0 auto;
                padding-top: 10px;
                padding-bottom: 10px;
                width: 20%;
            }
            .header {
                text-align: center;
            }
            </style>
            """, unsafe_allow_html=True)
            
            st.markdown(f"""
            <br>
            <div class="container">
                <div class="header">
                    <img src="data:image/png;base64,{image_base64}">
                </div>
            </div>
            <br>
            <br>
            <br>
            """, unsafe_allow_html=True)
        
        with buttons_placeholder.container():
            # Define the desired button width in pixels
            button_width = 200
            
            # Create columns with a specified width
            col1, col2, col3 = st.columns([1, button_width/100, 1])
            
            # Place the button in the middle column
            with col2:
                if st.button("Find A Doctor", key='1', help='Executes Find A Doctor', use_container_width=True):
                    st.session_state.action = "find_a_doctor"
                    
            # Create columns with a specified width
            col11, col22, col33= st.columns([1, button_width/100, 1])
            with col22:
                if st.button("Appointment Maker", key='2', help='Executes Appointment Maker', use_container_width=True):
                    st.session_state.action = "appointment_maker"
                    
            col111, col222, col333 = st.columns([1, button_width/100, 1])
            with col222:
                if st.button("Visit Assistant", key='3', help='Executes Visit Assistant', use_container_width=True):
                    st.session_state.action = "visit_assistant"
                    
            col1111, col2222, col3333 = st.columns([1, button_width/100, 1])
            with col2222:
                if st.button("Wellness Advocate", key='4', help='Executes Wellness Advocate', use_container_width=True):
                    st.session_state.action = "wellness_advocate"

    # Handle actions based on session state
    if st.session_state.action == "find_a_doctor":
        title_placeholder.empty()
        image_placeholder.empty()
        buttons_placeholder.empty()
        find_a_doctor()
    elif st.session_state.action == "appointment_maker":
        title_placeholder.empty()
        image_placeholder.empty()
        buttons_placeholder.empty()
        appointment_maker()
    elif st.session_state.action == "visit_assistant":
        title_placeholder.empty()
        image_placeholder.empty()
        buttons_placeholder.empty()
        visit_assistant()
    elif st.session_state.action == "wellness_advocate":
        title_placeholder.empty()
        image_placeholder.empty()
        buttons_placeholder.empty()
        wellness_advocate()

if __name__ == "__main__":
    main()
