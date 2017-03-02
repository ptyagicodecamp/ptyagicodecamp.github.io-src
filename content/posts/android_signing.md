Title: Automatic Android APK Signing
Date: 2016-12-20 12:51PM
Authors: ptyagi
Category: Development
Tags: android, gradle, signing, apk, dev
Summary: This post shows how build.gradle can be configured to sign Android APKs automatically without manual interventions.

### Declaring Signing credentials ###
Never put your signing apk credentials in github or any public sharable place. Always put them in a non-committable file. I'll be using local gradle installations's `gradle.properties` to store signing creds. It sits at root level of your project. Alternately, you can also use <path-to-.gradle-dir>/.gradle/.gradle.properties.

#### Declaring release apk credentials ####
```
RELEASE_KEYSTORE_FILE={path to your release keystore}
RELEASE_KEYSTORE_PASSWORD=*****
RELEASE_KEYSTORE_ALIAS=*****
```

#### Declaring debug apk credentials ####
```
DEBUG_KEYSTORE_FILE={path to your debug keystore}
DEBUG_KEYSTORE_PASSWORD=*****
DEBUG_KEYSTORE_ALIAS=*****
```
Note: There is no quotes around file path, passwords and alias.

### Loading variables from gradle.properties into build.gradle ###
```
Properties properties = new Properties()
properties.load(project.rootProject.file('gradle.properties').newDataInputStream())
def RELEASE_KEYSTORE_FILE = properties.getProperty('RELEASE_KEYSTORE_FILE')
def RELEASE_KEYSTORE_PASSWORD = properties.getProperty('RELEASE_KEYSTORE_PASSWORD')
def RELEASE_KEYSTORE_ALIAS = properties.getProperty('RELEASE_KEYSTORE_ALIAS')

def DEBUG_KEYSTORE_FILE = properties.getProperty('DEBUG_KEYSTORE_FILE')
def DEBUG_KEYSTORE_PASSWORD = properties.getProperty('DEBUG_KEYSTORE_PASSWORD')
def DEBUG_KEYSTORE_ALIAS = properties.getProperty('DEBUG_KEYSTORE_ALIAS')
```

### Defining Signing config in `build.gradle` ###
```
signingConfigs {
        debug {
            storeFile file(new File(DEBUG_KEYSTORE_FILE))
            storePassword DEBUG_KEYSTORE_PASSWORD
            keyAlias DEBUG_KEY_ALIAS
            keyPassword DEBUG_KEY_PASSWORD
        }

        release {
            storeFile file(new File(RELEASE_KEYSTORE_FILE))
            storePassword RELEASE_KEYSTORE_PASSWORD
            keyAlias RELEASE_KEY_ALIAS
            keyPassword RELEASE_KEY_PASSWORD
        }
    }
```

Note: Order of defining `buildTypes` block and `signingConfigs` block is very important. `signingConfigs` comes before `buildTypes` block.

### Putting All together ###
Full signing configuration in `build.gradle` will look like this:
```
apply plugin: 'com.android.application'

android {
    compileSdkVersion 22
    buildToolsVersion "22.0.1"

    defaultConfig {
        applicationId "com.myawesomeproject.id"
        minSdkVersion 14
        targetSdkVersion 24
        versionCode 1
        versionName "1.1"
    }

    signingConfigs {
        debug {
            storeFile file(new File(DEBUG_KEYSTORE_FILE))
            storePassword DEBUG_KEYSTORE_PASSWORD
            keyAlias DEBUG_KEY_ALIAS
            keyPassword DEBUG_KEY_PASSWORD
        }

        release {
            storeFile file(new File(RELEASE_KEYSTORE_FILE))
            storePassword RELEASE_KEYSTORE_PASSWORD
            keyAlias RELEASE_KEY_ALIAS
            keyPassword RELEASE_KEY_PASSWORD
        }
    }

    buildTypes {
        debug {
            signingConfig signingConfigs.debug
            minifyEnabled false
        }

        release {
            signingConfig signingConfigs.release
            minifyEnabled true
            proguardFiles getDefaultProguardFile('proguard-android.txt'), 'proguard-rules.pro'
        }
    }
} //closing android block


dependencies {
    compile fileTree(dir: 'libs', include: ['*.jar'])
}
```
