PROGRAM PLC_Drain_System
  VAR
    X_Sensor_ON AT %IX0.1 : BOOL;
  END_VAR
  VAR
    C_Buzer : BOOL;
  END_VAR
  VAR
    Y_Buzer AT %QX0.1 : BOOL;
  END_VAR
  VAR
    Delay : TIME := T#0.5S;
    TON0 : TON;
    TP0 : TP;
  END_VAR

  TP0(IN := NOT(X_Sensor_ON), PT := Delay);
  Y_Buzer := TP0.Q;
  C_Buzer := NOT(TP0.Q);
  TON0(IN := C_Buzer AND NOT(X_Sensor_ON), PT := Delay);
  X_Sensor_ON := TON0.Q;
END_PROGRAM


CONFIGURATION Config0

  RESOURCE Res0 ON PLC
    TASK task0(INTERVAL := T#20ms,PRIORITY := 0);
    PROGRAM instance0 WITH task0 : PLC_Drain_System;
  END_RESOURCE
END_CONFIGURATION
