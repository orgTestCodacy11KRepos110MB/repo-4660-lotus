import React, { useState } from "react";
import { Card, Input, Button, Form } from "antd";

interface LoginForm extends HTMLFormControlsCollection {
  username: string;
  password: string;
}

interface UserSignup {
  username: string;
  email: string;
  password: string;
}

interface FormElements extends HTMLFormElement {
  readonly elements: LoginForm;
}

type SignupProps = {
  onSubmit: (user: UserSignup) => void;
  hasInvite?: boolean;
};

const SignUp = (props: SignupProps) => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [email, setEmail] = useState("");

  const handleUserNameChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setUsername(event.target.value);
  };

  const handlePasswordChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setPassword(event.target.value);
  };
  const handleEmailChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setEmail(event.target.value);
  };
  const handleNewUser = (event: React.FormEvent<FormElements>) => {
    props.onSubmit({ username, email, password });
  };

  const cardTitle = props.hasInvite ? "Sign up to join the Team" : "Sign Up";

  return (
    <div>
      <Card title={cardTitle} className="flex flex-col">
        {/* <img src="../assets/images/logo_large.jpg" alt="logo" /> */}
        <Form onFinish={handleNewUser} name="create_organization">
          <Form.Item>
            <label htmlFor="username">Username</label>
            <Input
              type="text"
              name="organization_name"
              value={username}
              defaultValue="username123"
              onChange={handleUserNameChange}
            />
          </Form.Item>
          <Form.Item>
            <label htmlFor="username">Email</label>
            <Input
              type="email"
              name="email"
              value={email}
              defaultValue="elon@musk.com"
              onChange={handleEmailChange}
            />
          </Form.Item>
          <Form.Item>
            <label htmlFor="password">Password</label>
            <Input
              type="password"
              name="password"
              value={password}
              defaultValue="password123"
              onChange={handlePasswordChange}
            />
          </Form.Item>

          <Form.Item>
            <Button htmlType="submit">Register</Button>
          </Form.Item>
        </Form>
      </Card>
    </div>
  );
};

export default SignUp;
