import { useState } from "react";
import "../css/login.css"
import LoginLogo from "../img/logo.png";

export function Login() {
  const [error, setError] = useState(null);
  const [data, setData] = useState(null);

  const handleSubmit = async (event) => {
    event.preventDefault();

    const response = await fetch('http://127.0.0.1:8000/api2/api-token-auth/', {
      method: 'post',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data)
    });

    if (response.ok) {
      setData(await response.json());
    } else {
      setError(true)
    }
    };

    return (
        <div className="login-container">
            <img className="login-logo" src={LoginLogo} alt=""/>
            <form className="login-form" onSubmit={handleSubmit} method="post">
                <h1 className="login-title">Login</h1>
                <div className="login-label">
                    <i className="fa-solid fa-user"></i>
                    <input type="text" id="username" />
                </div>
                <div className="login-label">    
                    <i className="fa-solid fa-lock"></i>
                    <input type="password" id="password" />
                    {error && <div className="error-message">Los datos ingresados no son correctos</div>}
                </div>
                
                <button type="Submit" >Iniciar sesion</button>
            </form>
            
        </div>
    )
}