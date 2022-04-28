import React, {FC} from 'react';
import styles from './FormInput.module.css';

interface FormInputProps {
    title: string,
    setState: (val: any) => void
}

const FormInput: FC<FormInputProps> = ({
                                           title,
                                           setState,
                                       }) => {
        return (
            <div className={styles.FormInput} data-testid="FormInput">
                <div>
                    {title}
                    <input type="text"
                           onChange={e => setState(e.target.value)}
                    />
                </div>
            </div>
        )
    }
;

export default FormInput;
